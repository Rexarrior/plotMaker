import numexpr as ne


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


def compute_math(expr, vars):
    local_dict = {var.name: var.min for var in vars}
    index = 0
    
    while(local_dict[vars[-1].name] <= vars[-1].max):
        curr_res = evaluate_math_expr(expr, local_dict)
        if (not curr_res):
            raise Exception("evaluation of expression has failed")      
        yield (local_dict.copy(), curr_res[1])
        is_next_finding = True
        while(is_next_finding):
            name = vars[index].name
            local_dict[name] += vars[index].step
            if (local_dict[name] > vars[index].max):
                local_dict[name] = vars[index].min
                index += 1
                if (index == len(vars)):
                    break
            else:
                index = 0
                is_next_finding = False
