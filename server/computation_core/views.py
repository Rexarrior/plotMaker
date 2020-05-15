from django.shortcuts import render
from django.http import HttpResponse
import json
from computation_core.models import *
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def post_computation_task(request):
    json_string = request.POST.get('json_data')
    task = json.loads(json_string)
    expr = Expression(text=task['expression'],
                      name=task['expression_name'],
                      user_id=task['user_id'])
    expr.save()
    variables = task['variables']
    for var in variables:
        new_var = Variable(expr_fk=expr,
                           name=var['name'],
                           min=var['min'],
                           max=var['max'],
                           step=var['step']
                           )
        new_var.save()
    
    return HttpResponse(status=200)


@csrf_exempt
def get_expressions(request):
    user_id = request.GET.get('user_id')
    exprs = Expression.objects.filter(user_id=user_id)
    json_string = json.dumps(exprs)
    response = HttpResponse(json_string)
    return response


@csrf_exempt
def get_expr_status(request):
    expr_id = request.GET.get('expression_id')
    expression = Expression.objects.get(id=expr_id)
    response = HttpResponse(status=200)
    response['expression_status'] = expression.status
    return response


@csrf_exempt
def get_expr_solution(request):
    expr_id = request.GET.get('expression_id')
    expr = Expression.objects.get(id=expr_id)
    results = Result.objects.filter(expr_fk=expr)
    resp_results = []
    for res in results:
        resp_results.append((json.loads(res.args), res.result))
    response = HttpResponse(status=200)
    response.content = json.dumps(resp_results)


@csrf_exempt
def get_exrp_variables(request):
    expr_id = request.GET.get('expression_id')
    expr = Expression.objects.get(id=expr_id)
    variables = Variable.objects.filter(expr_fk=expr)
    resp_vars = []
    for var in variables:
        resp_vars.append(var)
    response = HttpResponse(status=200)
    response.content = json.dumps(resp_vars)
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