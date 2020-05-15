import sys


def is_numeric(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True


def declare_arg_vars():
    for arg in sys.argv:
        parts = arg.split('=')
        name = parts[0]
        value = parts[1]
        exec(f'{name} = {float(value)}')
