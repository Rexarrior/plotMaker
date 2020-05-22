import numexpr as ne
import sys
import requests
import json
import subprocess


class Math_var(object):
    min = 0
    max = 0
    step = 0
    name = ''

    def __init__(self, *args, **kwargs):
        self.name = args[0]
        self.min = args[1]
        self.max = args[2]
        self.step = args[3]


def to_numexpr_syntax(expr):
    return expr


def evaluate_math_expr(expr, arg_dict):
    expr = to_numexpr_syntax(expr)
    try:
        res = ne.evaluate(expr, local_dict=arg_dict)
    except Exception as error:
        return False, error
    return True, res


def compute_math(expr, mvars):
    local_dict = {var.name: var.min for var in mvars}
    index = 0
    
    while(local_dict[mvars[-1].name] <= mvars[-1].max):
        curr_res = evaluate_math_expr(expr, local_dict)
        if (not curr_res[0]):
            raise Exception("evaluation of expression has failed")      
        yield (local_dict.copy(), curr_res[1].tolist())
        is_next_finding = True
        while(is_next_finding):
            name = mvars[index].name
            local_dict[name] += mvars[index].step
            if (local_dict[name] > mvars[index].max):
                if (index >= len(mvars)-1):
                    break
                local_dict[name] = mvars[index].min
                index += 1
                
            else:
                index = 0
                is_next_finding = False


def mvars_from_json(json_mvars):
    mvars = json.loads(json_mvars)
    res = [Math_var(mvar['name'],
                    mvar['min'],
                    mvar['max'],
                    mvar['step']
                    ) for mvar in mvars]
    return res


def run_subprocess(expr, mvars, expr_pk, server_url):
    mvars_json = json.dumps(mvars)
    return subprocess.Popen(['python3', __file__,
                            expr, mvars_json,
                            str(expr_pk), server_url
                             ])


def run_remote(expr, mvars, expr_pk, server_url):
    mvars_json = json.dumps(mvars)
    vmid = 1234543
    cmd_parts = ['ansible-playbook',
                 './computation_core/ansible/launch.yml',
                 '--extra-vars',
                 'vmID=' + str(vmid),
                 '--extra-vars',
                 'expr=' + '"' + str(expr) + '"',
                 '--extra-vars',
                 'mvars=' + '"' + str(mvars_json) + '"',
                 '--extra-vars',
                 'expr_pk=' + str(expr_pk),
                 '--extra-vars',
                 'server_url=' + str(server_url),
                 
                 ]
    launch_result = subprocess.Popen(' '.join(cmd_parts),
                                     shell=True
                                     )


def main(argv):

    expression = argv[1]
    mvars_json = argv[2]
    mvars = mvars_from_json(mvars_json)
    expr_pk = int(argv[3])
    server_url = argv[4]
    results = list(compute_math(expression, mvars))
    
    print(results)
    params = {'pk': expr_pk, 'results': json.dumps(results)}
    requests.post(url=server_url, json=params)


if __name__ == '__main__':
    main(sys.argv)
    # expr = "x**2 + y**2"
    # mvars = [{'name': 'x', 'min': 1, 'max': 2, 'step': 1},
    #          {'name': 'y', 'min': 1, 'max': 3, 'step': 1},
    #          ]
    # mvars_json = json.dumps(mvars)
    # expr_pk = str(8)
    # server_addr = "localhost:8000/post_expr_solutions/"
    # res = list(compute_math(expr, mvars_obj))
    # print(run_subprocess(expr, mvars, expr_pk, server_addr).stdout)
    pass
