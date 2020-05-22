(function(t){function e(e){for(var r,i,o=e[0],p=e[1],l=e[2],c=0,d=[];c<o.length;c++)i=o[c],Object.prototype.hasOwnProperty.call(n,i)&&n[i]&&d.push(n[i][0]),n[i]=0;for(r in p)Object.prototype.hasOwnProperty.call(p,r)&&(t[r]=p[r]);u&&u(e);while(d.length)d.shift()();return a.push.apply(a,l||[]),s()}function s(){for(var t,e=0;e<a.length;e++){for(var s=a[e],r=!0,o=1;o<s.length;o++){var p=s[o];0!==n[p]&&(r=!1)}r&&(a.splice(e--,1),t=i(i.s=s[0]))}return t}var r={},n={app:0},a=[];function i(e){if(r[e])return r[e].exports;var s=r[e]={i:e,l:!1,exports:{}};return t[e].call(s.exports,s,s.exports,i),s.l=!0,s.exports}i.m=t,i.c=r,i.d=function(t,e,s){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:s})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var s=Object.create(null);if(i.r(s),Object.defineProperty(s,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var r in t)i.d(s,r,function(e){return t[e]}.bind(null,r));return s},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="/";var o=window["webpackJsonp"]=window["webpackJsonp"]||[],p=o.push.bind(o);o.push=e,o=o.slice();for(var l=0;l<o.length;l++)e(o[l]);var u=p;a.push([0,"chunk-vendors"]),s()})({0:function(t,e,s){t.exports=s("56d7")},"034f":function(t,e,s){"use strict";var r=s("85ec"),n=s.n(r);n.a},"52a0":function(t,e,s){},"56d7":function(t,e,s){"use strict";s.r(e);s("e260"),s("e6cf"),s("cca6"),s("a79d");var r=s("2b0e"),n=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{attrs:{id:"app"}},[s("Workspace")],1)},a=[],i=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[s("b-navbar",{staticClass:"navbar-main",attrs:{toggleble:"sd",fixed:"top",type:"dark",variant:"dark"}},[s("div",{staticClass:"navbar-header"},[s("h3",{staticClass:"navbar-caption"},[t._v("PlotMaker")])]),s("div",{staticClass:"user-panel"},[s("p",[t._v(t._s(t.UserName))])]),t.IsAuthorized?s("div",{staticClass:"login-panel"},[s("b-button",{attrs:{variant:"outline-primary"}},[t._v(" Sign Out ")])],1):s("div",{staticClass:"login-panel"},[s("b-button",{attrs:{variant:"outline-primary"}},[t._v(" Sign In ")]),s("b-button",{attrs:{variant:"outline-primary"}},[t._v(" Sign Up ")])],1)]),t.IsAuthorized?s("div",[s("b-jumbotron",{staticClass:"expr-list-card",attrs:{lead:"Список рассчетов"}},t._l(t.Expressions,(function(e){return s("b-card-group",{key:e.id},[s("b-card",{staticClass:"expr-card"},[s("b-card-header",[s("b-link",{on:{click:function(s){return t.pickExpr(e)}}},[t._v(t._s(e.fields.name))])],1),s("b-card-body",[s("p",[t._v(t._s(e.fields.text))])]),s("b-card-footer",[s("b-link",{on:{click:function(s){return t.deleteExpr(e)}}},[t._v("Удалить")])],1)],1)],1)})),1),s("b-jumbotron",{staticClass:"expr-work-area"},[s("b-tabs",{attrs:{"content-class":"mt-3"}},[s("b-tab",{attrs:{title:"Выражение",active:""}},[s("b-form",{on:{submit:t.onSubmit,reset:t.onReset}},[s("b-form-group",{attrs:{id:"input-group-1",label:"Вычислить","label-for":"input-1",description:"Выражение, которое будет вычислено"}},[s("b-form-input",{attrs:{id:"input-1",type:"text",required:"",placeholder:"sqrt(x**2 + y**2)"},model:{value:t.Expression.text,callback:function(e){t.$set(t.Expression,"text",e)},expression:"Expression.text"}})],1),s("b-form-group",{attrs:{id:"input-group-2",label:"Название выражения","label-for":"input-2"}},[s("b-form-input",{attrs:{id:"input-2",required:"",placeholder:"Distance"},model:{value:t.Expression.name,callback:function(e){t.$set(t.Expression,"name",e)},expression:"Expression.name"}})],1),s("b-form-group",{attrs:{id:"input-group-3",label:"Список переменных","label-for":"input-3"}},[s("b-form-input",{attrs:{id:"input-3",required:"",placeholder:"x:1,0.01, 10; y:-100, 10, 100; ",description:"Границы изменения переменных в выражении"},model:{value:t.RawVariables,callback:function(e){t.RawVariables=e},expression:"RawVariables"}})],1),s("b-button",{staticClass:"control-button",attrs:{type:"submit",variant:"primary"}},[t._v("Вычислить")]),s("br"),s("b-button",{staticClass:"control-button",attrs:{type:"reset",variant:"danger"}},[t._v("Очистить")])],1)],1),t.IsResults?s("b-tab",{staticClass:"results-table",attrs:{title:"Результаты"}},[s("b-container",{staticClass:"table-container",attrs:{fluid:""}},[s("b-table",{attrs:{items:t.Results,"caption-top":""}})],1)],1):t._e()],1)],1)],1):s("div",[s("h2",[t._v("Требуется авторизация")])])],1)},o=[],p=(s("99af"),s("b0c0"),s("ac1f"),s("1276"),s("498a"),s("bc3a")),l=s.n(p),u="http://"+window.location.hostname+"/api",c={new_expression_url:"".concat(u,"/new_expr/"),delete_expression_url:"".concat(u,"/delete_expr/"),get_expressions_url:"".concat(u,"/get_exprs/"),get_expression_status_url:"".concat(u,"/get_expr_status/"),get_expression_solutions:"".concat(u,"/get_expr_solutions/"),get_expression_variables:"".concat(u,"/get_expr_variables/"),signin_url:"".concat(u,"/signin/"),signup_url:"".concat(u,"/signup/"),update_timedout:15e3},d=s("5118"),b={name:"Workspace",data:function(){return{UserName:"SampleUser",UserId:1,IsAuthorized:!0,Expressions:[],RawVariables:"",Results:[],IsResults:!1,Expression:{name:"",text:"",variables:[],pk:void 0,status:void 0},DEBUG_OUT:""}},methods:{onSubmit:function(t){t.preventDefault();var e=this.RawVariables.split(";");this.Expression.variables=[];for(var s=0;s<e.length-1;s++){var r={name:"",min:0,step:0,max:0},n=e[s].split(","),a=n[0].split(":");r.name=a[0].trim(),r.min=parseInt(a[1]),r.step=parseInt(n[1]),r.max=parseInt(n[2]),this.Expression.variables.push(r)}var i={expr:this.Expression,user_id:this.UserId},o=this;l.a.post(c.new_expression_url,i).then((function(t){o.Expression.pk=t.data.pk,o.loadExprs(),o.checkResult()}))},onReset:function(t){t.preventDefault(),this.Expression.name="",this.Expression.text="",this.Expression.pk=void 0,this.Expression.status=void 0,this.Expression.variables=[],this.RawVariables="",this.Results=[],this.IsResults=!1},pickExpr:function(t){var e=this;l.a.get(c.get_expression_variables,{params:{pk:t.pk}}).then((function(s){e.Expression.name=t.fields.name,e.Expression.text=t.fields.text,e.Expression.pk=t.pk,e.Expression.name=t.fields.name,e.Expression.variables=s.data,e.Expression.status=t.fields.status,e.Results=[],e.RawVariables="";for(var r=0;r<e.Expression.variables.length;r++){var n=e.Expression.variables[r];e.RawVariables+="".concat(n.fields.name,": ").concat(n.fields.min,", ").concat(n.fields.step,", ").concat(n.fields.max,"; ")}e.checkResult()}))},deleteExpr:function(t){t.pk==this.Expression.pk&&(this.Expression.name="",this.Expression.text="",this.Expression.pk=void 0,this.Expression.status=void 0,this.Expression.variables=[],this.RawVariables="",this.Results=[],this.IsResults=!1);var e=this;l.a.post(c.delete_expression_url,{pk:t.pk}).then((function(){e.loadExprs()}))},loadExprs:function(){var t=this;l.a.request({url:c.get_expressions_url,params:{user_id:this.UserId},method:"GET"}).then((function(e){t.Expressions=e.data}))},expressionUpdateLoop:function(){this.loadExprs(),Object(d["setTimeout"])(this.expressionUpdateLoop,c.update_timedout)},checkResult:function(){if(void 0!==this.Expression&&void 0!==this.Expression.pk){var t=this,e={params:{pk:this.Expression.pk}};l.a.get(c.get_expression_status_url,e).then((function(s){"RE"==s.data.status&&l.a.get(c.get_expression_solutions,e).then((function(e){for(var s=e.data,r=[],n=0;n<s.length;n++)s[n][0]["Значение выражения"]=s[n][1],r.push(s[n][0]);t.Results=r,t.IsResults=!0}))}))}},checkResultLoop:function(){this.checkResult(),Object(d["setTimeout"])(this.checkResultLoop,c.update_timedout)}},created:function(){this.expressionUpdateLoop(),this.checkResultLoop()}},f=b,x=(s("eb4d"),s("2877")),h=Object(x["a"])(f,i,o,!1,null,"4e931fb0",null),v=h.exports,m={name:"app",components:{Workspace:v}},_=m,g=(s("034f"),Object(x["a"])(_,n,a,!1,null,null,null)),E=g.exports,k=s("5f5b"),R=s("b1e0");s("f9e3"),s("2dd8");r["default"].config.productionTip=!1,r["default"].use(k["a"]),r["default"].use(R["a"]),new r["default"]({render:function(t){return t(E)}}).$mount("#app")},"85ec":function(t,e,s){},eb4d:function(t,e,s){"use strict";var r=s("52a0"),n=s.n(r);n.a}});
//# sourceMappingURL=app.5a2fe6a7.js.map