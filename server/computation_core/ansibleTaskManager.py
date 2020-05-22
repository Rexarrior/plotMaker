# encoding: utf-8
import django
import os
import sys
from computation_core import utils
import subprocess


sys.path.append('../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()


def run_task_task(expr_pk, cmd_arg):
    free_nodes = utils.get_free_work_nodes()
    if (len(free_nodes) <= 0):
        utils.launch_new_work_node()
        free_nodes = utils.get_free_work_nodes()
    node = free_nodes[0]
    node.is_free = False
    node.expr_pk = expr_pk
    node.save()
    cmd_arg += '--extra-vars vmID=' + str(node.vmid),
    launch_result = subprocess.Popen(cmd_arg,
                                     shell=True
                                     )
    launch_result.wait()


def terminate_task():
    utils.terminate_extra_nodes()


if __name__ == "__main__":
    mode = int(sys.argv[1])
    if (mode == 0):
        run_task_task(int(sys.argv[2]), sys.argv[3])
    elif (mode == 1):
        terminate_task()
    
