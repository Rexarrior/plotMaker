from django.urls import include, path
from computation_core.views import *

urlpatterns = [
    path('/api/signup/', post_new_user),
    path('/api/signin/', post_login),
    path('/api/new_expr/', post_computation_task),
    path('/api/delete_expr/', delete_expr),
    path('/api/get_exprs/', get_expressions),
    path('/api/get_expr_status/', get_expr_status),
    path('/api/get_expr_solutions/', get_expr_solution),
    path('/api/post_expr_solutions/', post_expr_solution),
    path('/api/get_expr_variables/', get_exrp_variables),
    path('/api/change_var/', post_changed_variable),
]