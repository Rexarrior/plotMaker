const server_url = 'http://188.119.67.69:8000/api/';
// const server_url = '/api/';

export default {
    new_expression_url : `${server_url}/new_expr/`,
    delete_expression_url : `${server_url}/delete_expr/`,
    get_expressions_url : `${server_url}/get_exprs/`,
    get_expression_status_url : `${server_url}/get_expr_status/`,
    get_expression_solutions : `${server_url}/get_expr_solutions/`,
    get_expression_variables : `${server_url}/get_expr_variables/`,
    signin_url : `${server_url}/signin/`,
    signup_url : `${server_url}/signup/`,
    update_timedout : 15000,
};