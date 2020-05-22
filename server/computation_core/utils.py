import subprocess
from computation_core.models import *
import random as rnd


PARAM_WORK_NODES_OPTIMUM = 3


def get_new_vmid():
    existing_vmids = [node.vmid for node in WorkNode.objects.all()]
    new_vmid = rnd.randint(0, 10000)
    while(new_vmid in existing_vmids):
        new_vmid = rnd.randint(0, 10000)
    return new_vmid


def get_free_work_nodes():
    return WorkNode.objects.filter(is_free=True)


def launch_new_work_node():
    vmid = get_new_vmid()
    cmd_parts = [
        'ansible-playbook',
        '/root/plotMaker/server/computation_core/ansible/launch.yml',
        '--extra-vars',
        'vmID=' + str(vmid),
    ]
    subprocess.Popen(' '.join(cmd_parts), shell=True)
    WorkNode(vmid=vmid).save()
    return vmid


def terminate_work_node(vmid):
    WorkNode.objects.get(vmid=vmid).delete()
    cmd_parts = [
        'ansible-playbook',
        '/root/plotMaker/server/computation_core/ansible/terminate.yml',
        '--extra-vars',
        'vmID=' + str(vmid),
    ]
    subprocess.Popen(' '.join(cmd_parts), shell=True)


def terminate_extra_nodes():
    free_nodes = get_free_work_nodes()
    if (len(free_nodes) <= PARAM_WORK_NODES_OPTIMUM):
        return
    for i in range(0, len(free_nodes) - PARAM_WORK_NODES_OPTIMUM):
        terminate_work_node(free_nodes[i].vmid)