"""Defines the functions for generating Mesos tasks"""
from __future__ import unicode_literals

import logging
from django.conf import settings


logger = logging.getLogger(__name__)

RESOURCE_TYPE_SCALAR = 'SCALAR'
CONTAINER_TYPE_DOCKER = 'DOCKER'
NETWORK_TYPE_BRIDGE = 'BRIDGE'


def create_mesos_task(task):
    """Creates and returns a Mesos task from a Scale task

    :param task: The task
    :type task: :class:`job.tasks.base_task.Task`
    :returns: JSON TaskInfo instance
    :rtype: dict
    """

    if task.uses_docker:
        return _create_docker_task(task)

    return _create_command_task(task)


def _create_base_task(task):
    """Creates and returns a base Mesos task from a Scale task

    :param task: The task
    :type task: :class:`job.tasks.base_task.Task`
    :returns: The base Mesos task
    :rtype: dict
    """

    mesos_task = {
        'task_id': {'value': task.id },
        'agent_id': {'value': task.agent_id},
        'name': task.name,
        'command': {},
        'resources': []
    }

    resources = task.get_resources()

    if settings.CONFIG_URI:
        mesos_task['command'] = {'uris': [{'value': settings.CONFIG_URI}]}

    task_resources = mesos_task['resources']
    for resource in resources.resources:
        if resource.value > 0.0:
            task_resource = {}
            task_resource['name'] = resource.name
            task_resource['type'] = RESOURCE_TYPE_SCALAR
            task_resource['scalar'] = {'value': resource.value}
            task_resources.append(task_resource)

    return mesos_task


def _create_command_task(task):
    """Creates and returns a command-line Mesos task from a Scale task

    :param task: The task
    :type task: :class:`job.tasks.base_task.Task`
    :returns: The command-line Mesos task
    :rtype: dict
    """

    mesos_task = _create_base_task(task)
    command = task.command if task.command else 'echo'
    if task.command_arguments:
        command += ' ' + task.command_arguments

    mesos_task['command'].update(
        {'value': command}
    )

    return mesos_task


def _create_docker_task(task):
    """Creates and returns a Dockerized Mesos task from a Scale task

    :param task: The task
    :type task: :class:`job.tasks.base_task.Task`
    returns: The Dockerized Mesos task
    :rtype: dict
    """

    mesos_task = _create_base_task(task)
    mesos_task['command'].update(
        {
            'shell': False,
            'arguments': [x for x in task.command_arguments.split(" ")]
        }
    )
    mesos_task['container'] = {
        'type': CONTAINER_TYPE_DOCKER,
        'docker': {
            'image': task.docker_image,
            'parameters': [],
            'network': NETWORK_TYPE_BRIDGE,
            'force_pull_image': False
        },
    }

    for param in task.docker_params:
        mesos_task['container']['docker']['parameters'].append({'key': param.flag, 'value': param.value})

    # TODO: Remove this once docker privileged is removed.
    if task.is_docker_privileged:
        mesos_task['container']['docker']['privileged'] = True

    return mesos_task
