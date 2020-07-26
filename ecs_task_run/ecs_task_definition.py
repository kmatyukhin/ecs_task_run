"""Run task in Amazon Elactic Container Service"""
import sys
import boto3
import json


_CONTAINER_DEFINITIONS_TEMPLATE=json.loads("""
{
    "name": "",
    "image": "",
    "repositoryCredentials": {
        "credentialsParameter": ""
    },
    "cpu": 0,
    "memory": null,
    "memoryReservation": null,
    "links": [],
    "portMappings": [],
    "essential": true,
    "entryPoint": [],
    "command": [],
    "environment": [],
    "environmentFiles": null,
    "mountPoints": [],
    "volumesFrom": [],
    "linuxParameters": {
        "capabilities": {
            "add": null,
            "drop": null
        },
        "devices": [],
        "initProcessEnabled": true,
        "sharedMemorySize": null,
        "tmpfs": null,
        "maxSwap": null,
        "swappiness": null
    },
    "secrets": null,
    "dependsOn": null,
    "startTimeout": null,
    "stopTimeout": null,
    "hostname": null,
    "user": null,
    "workingDirectory": null,
    "disableNetworking": null,
    "privileged": false,
    "readonlyRootFilesystem": false,
    "dnsServers": [],
    "dnsSearchDomains": [],
    "extraHosts": [],
    "dockerSecurityOptions": [],
    "interactive": false,
    "pseudoTerminal": false,
    "dockerLabels": {},
    "ulimits": [],
    "logConfiguration": {
        "logDriver": "awslogs",
        "options": {
            "awslogs-group": "",
            "awslogs-region": "",
            "awslogs-stream-prefix": ""
        },
        "secretOptions": null
    },
    "healthCheck": null,
    "systemControls": null,
    "resourceRequirements": null,
    "firelensConfiguration": null
}
""")

class ECSTaskDefinition:
    params = {}
    def __init__(self, *args, ecs_client=None, **kwargs):
        self.params = kwargs

        self.ecs_client = (
            ecs_client if ecs_client is not None
            else boto3.client("ecs", region_name=self.params['aws_region']))

        self.container_definitions = _CONTAINER_DEFINITIONS_TEMPLATE.copy()
        self.container_definitions['image'] = self.params['image']

    def register(self):
        return self.ecs_client.register_task_definition(
            containerDefinitions=(),
            family='family')

