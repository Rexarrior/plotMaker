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
         <b-card-group v-for="expr in Expresions" :key="expr.id">
         <b-card class="expr-card">
           <b-card-header>
              {{expr.name}}
           </b-card-header>
           <b-card-body>
             <p>{{expr.text}}</p>
           </b-card-body>
           <b-card-footer>
             <b-button @click="pickExpr(arg, event)" variant="outline-primary">
               Выбрать
             </b-button>
           </b-card-footer>
         </b-card>
         </b-card-group>
    </b-jumbotron>

    <b-jumbotron class="expr-work-area" >
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

      <b-form-group id="input-group-2" label="Описание выражения" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="Expression.name"
          required
          placeholder="Distance"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Список переменных" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="RawVariables"
          required
          placeholder="x:1,0.01, 10; y:-100, 10, 100; "
          description="Границы изменения переменных в выражении"

        ></b-form-input>
      </b-form-group>

      
      

        <b-button type="submit" variant="primary" class="control-button">Вычислить</b-button>
        <br>
        <b-button type="reset" variant="danger" class="control-button">Новое выражение</b-button>
    </b-form>
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
import func from './vue-temp/vue-editor-bridge';


export default {
  name: 'Workspace',
  
  data: function () {
    return {
      UserName: "SampleUser",
      IsAuthorized: true,
      Expresions:[],
      RawVariables:"",
      Expression:{
          name: "",
          text: "",
          variables: [],
        },
      //DEBUG_OUT:"",
    }
    
  },

  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      let parts = this.RawVariables.split(";");
      
      for (let i = 0; i < parts.length; i++)
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
        this. Expression.variables.push(variable);
      }
      let json = JSON.stringify(this.Expression);
      axios.post(consts.new_expression_url, {"json_data": json})
           .then(function(request){
              //console.log(request);
              if (request.status != 200)
                alert("ERROR - status isn't OK");
            })
           

    },
    onReset(evt) {
      evt.preventDefault();
      this.Expression.name = "";
      this.Expression.text = "";
      this.Expression.variables = [];
      this.RawVariables = "";
     },
    pickExpr(event){
      event.preventDefault();
      //console.log("!!");
    },
    expressionUpdateLoop(){

      axios.get(consts.get_expressions_url, {"user_id": 1})
           .then(function(response){
             this.DEBUG_OUT = response
           });
      setTimeout(expressionUpdateLoop, 15000);
    }
  },
  // created: function () {
  //   expressionUpdateLoop();
  // }

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
  padding-bottom: 10%;
  width: 25%;
  height: 70%;
  font-size: 20;

}
.expr-work-area{
  position: absolute;
  width: 50%;
  height: 70%;
  left:35%;
  top:10%;
  padding-bottom: 10%;
}


</style>
