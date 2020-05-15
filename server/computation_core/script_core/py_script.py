from script_parts import *
import subprocess


class Script(object):
    in_vars = []
    out_vars = None
    body = []
    out_type = "std"
    txt = None

    def __init__(self, *args, **kwargs):
        self.in_vars = args[0]
        self.body = args[1]
        if len(args) > 2:
            self.out_type = args[2]
        if len(args) > 3:
            self.out_vars = args[3]        

    def run_local(self, var_args):
        if (self.out_type == 'std'):
            with open('running_script.py', 'wt', encoding="utf-8") as f:
                f.write(self.txt)


def make_script(var, body, out_type="std", out_var=None):
    '''
    var:        variable section. Should be dict of var name - var value,
                value should be numeric
    body:       python script, include "import" section.
    out_type:   type of script out.
                If type == "std", no additional out will be created
                If type == "func", will be created out in format
                "out_var_1 = str(out_val_1),..."
                If type == "plot" will be created out in
                format of one numeric value.
                Out var shoul be presented in out_var
    out_var:    ouput variable names. related to out_type.
    '''
    txt = ''
    if out_type == "std":
        txt = make_stdout_script(var, body)
    elif out_type == "func":
        txt = make_funcout_script(var, body, out_var)
    elif txt == "plot":
        out_type = make_plotout_script(var, body, out_var)
    return Script(var, body, out_type, out_var, txt)


def make_stdout_script(var, body):
    txt = ''
    txt += ARGS_PARSE_SCRIPT
    txt += f'exec({body})\n'
    return txt


def make_funcout_script(var, body, out_var):
    func_args_str = var_arr_to_var_str(var)
    func_ret_str = var_arr_to_var_str(out_var)
    txt = ''    
    txt += f'def script_func({func_args_str}):\n'
    txt += f'  exec(body)\n'
    txt += f'  return {func_ret_str}'
    return txt


def make_plotout_script(var, body, out_var):
    return make_funcout_script(var, body, out_var)


def var_arr_to_var_str(var):
    return ', '.join([str(variable) for variable in var])
