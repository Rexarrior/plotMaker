<template>
  <div>
    <b-navbar toggleble="sd"  fixed="top" type="dark" variant="dark"  class = "navbar-main">
      <div class="navbar-header">
        <h3 class="navbar-caption">PlotMaker</h3>
      </div>
      <div class="user-panel">
        
        <p>{{UserName}}</p>
      </div>
      <div class="login-panel" v-if="IsAuthorized">
        <b-button variant="outline-primary">
          Sign Out
        </b-button>
        
      </div>
      <div class="login-panel" v-else>
        <b-button variant="outline-primary">
          Sign In
        </b-button>
        <b-button variant="outline-primary">
          Sign Up
        </b-button>
        </div>
    </b-navbar>
  
  <div v-if="IsAuthorized">
    <b-jumbotron  class="expr-list-card" lead="Список рассчетов">
         <!-- <p>{{DEBUG_OUT}}</p> -->
         <b-card-group v-for="expr in Expressions" :key="expr.id">
         <b-card class="expr-card">
           <b-card-header >
              <b-link @click="pickExpr(expr)">{{expr.fields.name}}</b-link>
           </b-card-header>
           <b-card-body>
             <p>{{expr.fields.text}}</p>
           </b-card-body>
           <b-card-footer>
             <b-link @click="deleteExpr(expr)">Удалить</b-link>
           </b-card-footer>
           
         </b-card>
         </b-card-group>
    </b-jumbotron>

    <b-jumbotron class="expr-work-area" >
      <b-tabs content-class="mt-3">
        <b-tab title="Выражение" active>
          <b-form @submit="onSubmit" @reset="onReset">
          <b-form-group
            id="input-group-1"
            label="Вычислить"
            label-for="input-1"
            description="Выражение, которое будет вычислено"
          >
            <b-form-input
              id="input-1"
              v-model="Expression.text"
              type="text"
              required
              placeholder="sqrt(x**2 + y**2)"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Название выражения" label-for="input-2">
            <b-form-input
              id="input-2"
              v-model="Expression.name"
              required
              placeholder="Distance"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3" label="Список переменных" label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="RawVariables"
              required
              placeholder="x:1,0.01, 10; y:-100, 10, 100; "
              description="Границы изменения переменных в выражении"

            ></b-form-input>
          </b-form-group>

          
          

            <b-button type="submit" variant="primary" class="control-button">Вычислить</b-button>
            <br>
            <b-button type="reset" variant="danger" class="control-button">Очистить</b-button>
          </b-form>
        </b-tab>
        <b-tab title="Результаты" v-if="IsResults" class="results-table">
           <b-container fluid class="table-container">
            <b-table
              :items="Results" 
              caption-top
            >
            </b-table>
           </b-container>
          </b-tab>
      </b-tabs>
    </b-jumbotron>
  </div>
  
  <div v-else>
    <h2>Требуется авторизация</h2>
  </div>
  
  </div>

</template>

<script>
import axios from "axios"
import consts from "../consts"
import { setTimeout } from 'timers';


export default {
  name: 'Workspace',
  
  data: function () {
    return {
      UserName: "SampleUser",
      UserId:1,
      IsAuthorized: true,
      Expressions:[],
      RawVariables:"",
      Results: [],
      IsResults: false,
      Expression:{
          name: "",
          text: "",
          variables: [],
          pk: undefined,
          status: undefined,
          
        },
      DEBUG_OUT:"",
    }
    
  },

  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      

      let parts = this.RawVariables.split(";");
      this.Expression.variables = [];
      for (let i = 0; i < parts.length-1; i++)
      {
        let variable = {
          name:"",
          min:0,
          step:0,
          max:0,
        }
        let subparts = parts[i].split(",");
        let first_subparts = subparts[0].split(":");
        variable.name = first_subparts[0].trim();
        variable.min = parseInt(first_subparts[1]);
        variable.step = parseInt(subparts[1]);
        variable.max = parseInt(subparts[2]);
        this.Expression.variables.push(variable);
      }
      let data = {expr: this.Expression, user_id: this.UserId}
      let instance = this;
      axios.post(consts.new_expression_url, data)
           .then(function(responce){
              instance.Expression.pk =  responce.data.pk;
              instance.loadExprs();
              instance.checkResult();
            });
           

    },
    onReset(evt) {
      evt.preventDefault();
      this.Expression.name = "";
      this.Expression.text = "";
      this.Expression.pk = undefined;
      this.Expression.status = undefined;
      this.Expression.variables = [];
      this.RawVariables = "";
      this.Results = [];
      this.IsResults = false;

     },


    pickExpr(arg){
        let instance = this;
        axios.get(consts.get_expression_variables,
                  {'params':{'pk':arg.pk}})
             .then(function(response){
                instance.Expression.name = arg.fields.name;
                instance.Expression.text = arg.fields.text;
                instance.Expression.pk = arg.pk;
                instance.Expression.name = arg.fields.name;
                instance.Expression.variables = response.data;
                instance.Expression.status = arg.fields.status;
                instance.Results = [];
                instance.RawVariables = "";
                for(let i = 0; i < instance.Expression.variables.length; i++)
                {
                  let variable = instance.Expression.variables[i]
                  instance.RawVariables += `${variable.fields.name}: ${variable.fields.min}, ${variable.fields.step}, ${variable.fields.max}; `
                }
                instance.checkResult();
             });
    },
    deleteExpr(arg){
      if (arg.pk == this.Expression.pk)
      {
          this.Expression.name = "";
          this.Expression.text = "";
          this.Expression.pk = undefined;
          this.Expression.status = undefined;
          this.Expression.variables = [];
          this.RawVariables = "";
          this.Results = [];
          this.IsResults = false;
      }
      let instance = this;
      axios.post(consts.delete_expression_url, {'pk':arg.pk}).then(function(){
             
            instance.loadExprs();
      });
     

    },
    loadExprs(){
      
      let instance = this;
      axios.request({
        'url':consts.get_expressions_url,
        'params':{'user_id':this.UserId},
        'method':'GET'
      })
      .then(function(response){
        instance.Expressions = response.data;
      });
    },
    expressionUpdateLoop(){
      this.loadExprs();
      setTimeout(this.expressionUpdateLoop, consts.update_timedout);
    },
    checkResult(){
      if (this.Expression === undefined || this.Expression.pk === undefined)
      {
        return;
      }
      let instance = this;
      let params = {params: {'pk': this.Expression.pk}};
      axios.get(consts.get_expression_status_url, params).then(function(responce){
          if (responce.data.status == "RE")
          {
            axios.get(consts.get_expression_solutions, params).then(function(responce2){
              let results = responce2.data;
              let formatted_results = [];
              for(let i =0; i < results.length; i++)
              {
                results[i][0]['Значение выражения'] = results[i][1];
                formatted_results.push(results[i][0]);
              }
              instance.Results = formatted_results;
              instance.IsResults = true;
            });
          }
      });
    },
    checkResultLoop(){
      this.checkResult();
      setTimeout(this.checkResultLoop, consts.update_timedout)
    }
  },
  created: function () {
    this.expressionUpdateLoop();
    this.checkResultLoop();
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar-caption{
  color: white;
}

.user-panel{
  padding-left: 75%;
  margin-right: 1%;
  margin-top: 10px;
  color:white;
}

.login-panel{
 
  max-width: 150px;
  min-width: 150px;
}


.expr-list-card{
  position: absolute;
  left: 5%;
  top: 10%;
  bottom: 5%;
  padding-bottom: 10%;
  width: 25%;
  font-size: 20;

}
.expr-work-area{
  position: absolute;
  left: 35%;
  top: 10%;
  bottom: 5%;
  padding-bottom: 10%;
  width: 45%;
  font-size: 20;
}

.table-container {
     height: calc(100vh - 450px);
}
 .table-container table {
     display: flex;
     flex-flow: column;
     height: 100%;
     width: 100%;
}
 .table-container table thead {
     flex: 0 0 auto;
     width: 100%;
}
 .table-container table tbody {
     flex: 1 1 auto;
     display: block;
     width: 100%;
     overflow-y: auto;
}
 .table-container table tbody tr {
     width: 100%;
}
 .table-container table thead, .table-container table tbody tr {
     display: table;
     table-layout: fixed;
}
 .table-container table {
     border-collapse: collapse;
}
 .table-container table td, .table-container table th {
     padding: 0.4em;
}
 .table-container table th {
     border: 1px solid black;
     font-size: 0.7vw;
}
 .table-container table td {
     border: 1px solid #e7e1e1;
     font-size: 0.85em;
    /* necessary to set for proper "showing row x of y" calculations if infinate scoll */
     white-space: nowrap;
     text-align: center;
     padding: 10px 5px;
     white-space: nowrap;
     text-overflow: ellipsis;
}
 .table-container table thead {
     border: 2px solid #0F0FA3;
}
 .table-container th {
     background-color: #0F0FA3;
     color: #b5aba4;
     cursor: pointer;
     -webkit-user-select: none;
   -moz-user-select: none !important;
     -ms-user-select: none;
     user-select: none;
}
 .table-container table tbody td {
     padding: 8px;
     cursor: pointer;
}
 .table-container table tbody tr:hover {
     background-color: rgba(168, 168, 239, .5);
}
 .table-container table thead td {
     padding: 10px 5px;
}
 .table-container tr:nth-child(even) {
     background-color: rgba(168, 168, 239, 1);
}

/* START Adjustments for width and scrollbar hidden */
 .table-container th.table-action, .table-container td.table-action {
     width: 5.8vw;
}
 .table-container table thead {
     width: calc(100% - 1px);
}
 .table-container table tbody::-webkit-scrollbar {
     width: 1px;
}
 .table-container table tbody::-webkit-scrollbar {
     width: 1px;
}
 .table-container table tbody::-webkit-scrollbar-thumb {
     width: 1px;
}
/* END Adjustments for width and scrollbar */
</style>
