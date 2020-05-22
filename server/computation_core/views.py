from django.shortcuts import render
from django.http import HttpResponse
import json
from computation_core.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from computation_core.math_core import run_subprocess, run_remote
import computation_core.utils as utils

APP_POST_RESULT = "http://rexarrior.ml/api/post_expr_solutions/"


def djObject_to_json(obj):
    return serializers.serialize('json', obj)


@csrf_exempt
def delete_expr(request):
    data = json.loads(request.body)
    pk = data['pk']
    founded = Expression.objects.filter(pk=pk)
    if (len(founded) > 0):
        # print("{} deleted".format(len(founded)))
        founded.delete()
    return HttpResponse(status=200)


@csrf_exempt
def post_computation_task(request):
    json_string = request.body
    data = json.loads(json_string)
    task = data['expr']
    expr = Expression(text=task['text'],
                      name=task['name'],
                      user_id=data['user_id'],
                      status=Expression.COMPUTING)
    expr.save()
    variables = task['variables']
    run_remote(node.vmid, task['text'], variables,
               expr.pk, APP_POST_RESULT)
    
    for var in variables:
        new_var = Variable(expr_fk=expr,
                           name=var['name'],
                           min=var['min'],
                           max=var['max'],
                           step=var['step']
                           )
        new_var.save()
    data = json.dumps({'pk': expr.pk})
    return HttpResponse(data, status=200)


@csrf_exempt
def get_expressions(request):
    user_id = request.GET.get('user_id')
    # print('user_id={}'.format(user_id))
    exprs = Expression.objects.filter(user_id=user_id)
    json_string = djObject_to_json(exprs)
    response = HttpResponse(json_string)
    return response


@csrf_exempt
def get_expr_status(request):
    pk = request.GET.get('pk')
    expression = Expression.objects.get(pk=pk)
    jsonString = json.dumps({'status': expression.status})
    response = HttpResponse(jsonString, status=200)
    return response


@csrf_exempt
def get_expr_solution(request):
    pk = request.GET.get('pk')
    expr = Expression.objects.get(pk=pk)
    results = Result.objects.filter(expr_fk=expr)
    resp_results = []
    for res in results:
        resp_results.append((json.loads(res.args), res.result))
    json_str = json.dumps(resp_results)
    response = HttpResponse(json_str, status=200)
    return response


@csrf_exempt
def post_expr_solution(request):
    data = json.loads(request.body.decode('utf-8'))
    expr = Expression.objects.get(pk=data['pk'])
    results = json.loads(data['results'])
    for res in results:
        new_res = Result(expr_fk=expr, args=json.dumps(res[0]),
                         result=res[1])
        new_res.save()
    expr.status = Expression.READY
    expr.save()
    node = WorkNode.objects.get(expr_pk=expr.pk)
    node.is_free = True
    node.expr_pk = -1
    node.save()
    utils.terminate_extra_nodes_parallel()
    return HttpResponse(status=200)
    

@csrf_exempt
def get_exrp_variables(request):
    pk = request.GET.get('pk')
    expr = Expression.objects.get(pk=pk)
    variables = Variable.objects.filter(expr_fk=expr)
    resp_vars = []
    for var in variables:
        resp_vars.append(var)
    response = HttpResponse(status=200)
    response.content = djObject_to_json(resp_vars)
    return response


@csrf_exempt
def post_changed_variable(request):
    json_string = request.POST.get('json_data')
    changes = json.loads(json_string)
    var = Variable.objects.get(id=changes['id'])
    var.min = changes['min']
    var.max = changes['max']
    var.step = changes['step']
    var.name = changes['name']
    var.save()
    return HttpResponse(status=200)


@csrf_exempt
def post_new_user(request):
    json_string = request.POST.get('json_data')
    user_data = json.loads(json_string)
    name = user_data['user_name']
    password = user_data["password"]
    user = User(name=name, password=password)
    user.save()
    return HttpResponse(status=200)


@csrf_exempt
def post_login(request):
    json_string = request.POST.get('json_data')
    user_data = json.loads(json_string)
    name = user_data['user_name']
    password = user_data["password"]
    query = User.objects.filter(name=name)
    result = False
    if (len(query) > 0):
        user = query.get(name=name)
        if (user.password == password):
            result = True
    response = HttpResponse(status=200)
    response['result'] = result
    return response