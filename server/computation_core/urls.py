from django.urls import include, path
from computation_core.views import *
urlpatterns = [
    path('signup/', post_new_user),
    path('signin/', post_login),
    path('new_expr/', post_computation_task),
    path('delete_expr/', delete_expr),
    path('get_exprs/', get_expressions),
    path('get_expr_status/', get_expr_status),
    path('get_expr_solutions/', get_expr_solution),
    path('get_expr_variables/', get_exrp_variables),
    path('change_var/', post_changed_variable),
]