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
        self.min = float(args[1])
        self.max = float(args[2])
        self.step = float(args[3])


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
    json_mvars = json_mvars.replace("'", '"')
    mvars = json.loads(json_mvars)
    res = [Math_var(mvar['name'],
                    mvar['min'],
                    mvar['max'],
                    mvar['step']
                    ) for mvar in mvars]
    return res


def run_subprocess(expr, mvars, expr_pk, server_url):
    mvars_coded = encode_mvars(mvars)
    return subprocess.Popen(['python3', __file__,
                            expr, mvars_coded,
                            str(expr_pk), server_url
                             ])


def encode_mvars(mvars):
    return "---".join([f'{mvar["name"]}&' +
                       f'{mvar["min"]}&' +
                       f'{mvar["max"]}&' +
                       f'{mvar["step"]}&'
                       for mvar in mvars
                       ])


def decode_mvars(mvars_coded):
    mvar_codes = mvars_coded.split("---")
    res = []
    for code in mvar_codes:
        mvar_values = code.split("&")
        res.append(Math_var(mvar_values[0],
                            mvar_values[1],
                            mvar_values[2],
                            mvar_values[3]
                            )
                   )
    return res


def run_remote(expr, mvars, expr_pk, server_url):
    mvars_coded = encode_mvars(mvars)
    expr = expr.replace(" ", "")       
    cmd_parts = [
        'python3',
        '/root/plotMaker/server/ansibleTaskManager.py',
        '0',
        expr,
        mvars_coded,
        str(expr_pk),
        server_url
    ]
    print(f'run command: {str(cmd_parts)}')
    launch_result = subprocess.Popen(" ".join(cmd_parts),
                                     shell=True
                                     )


def main(argv):
    print(f"argv={str(argv)}")
    expression = argv[1]
    mvars_coded = argv[2]
    mvars = decode_mvars(mvars_coded)
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
    # mvars_coded = json.dumps(mvars)
    # expr_pk = str(8)
    # server_addr = "localhost:8000/post_expr_solutions/"
    # res = list(compute_math(expr, mvars_obj))
    # print(run_subprocess(expr, mvars, expr_pk, server_addr).stdout)
    pass
