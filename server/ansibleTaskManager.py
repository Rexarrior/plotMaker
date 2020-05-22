# encoding: utf-8
import django
import os
import sys
import subprocess
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()
from computation_core import utils


def run_task_task(expr, mvars_coded, expr_pk, server_url):
    free_nodes = utils.get_free_work_nodes()
    if (len(free_nodes) <= 0):
        utils.launch_new_work_node()
        free_nodes = utils.get_free_work_nodes()
    node = free_nodes[0]
    node.is_free = False
    node.expr_pk = expr_pk
    node.save()
    cmd_parts = ['ansible-playbook',
                 '/root/plotMaker/server/' +
                 'computation_core/ansible/run_task.yml',               
                 '--extra-vars',
                 '--extra-vars',
                 'vmID=' + str(node.vmid),
                 'expr=' + '"' + str(expr) + '"',
                 '--extra-vars',
                 'mvars=' + '"' + str(mvars_coded) + '"',
                 '--extra-vars',
                 'expr_pk=' + str(expr_pk),
                 '--extra-vars',
                 'server_url=' + str(server_url),
                 ]
    cmd_arg = " ".join(cmd_parts)
    print(f'run command: {cmd_arg}')
    launch_result = subprocess.Popen(cmd_arg,
                                     shell=True
                                     )
    launch_result.wait()


def terminate_task():
    utils.terminate_extra_nodes()


if __name__ == "__main__":
    argv = sys.argv
    print(f'argv={str(argv)}')
    mode = int(argv[0])
    if (mode == 0):
        run_task_task(argv[2],
                      argv[3],
                      int(argv[4]),
                      argv[5]
                      )
    elif (mode == 1):
        terminate_task()
