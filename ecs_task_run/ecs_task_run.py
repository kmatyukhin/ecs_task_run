"""Run task in Amazon Elactic Container Service"""
import sys
import boto3
from .ecs_task_definition import ECSTaskDefinition


class ECSTaskRun:
    params = {}
    def __init__(self, *args, sts_client=None, ecs_client=None, **kwargs):
        self.params = kwargs
        self.sts_client = (
            sts_client if sts_client is not None
            else boto3.client("sts", region_name=kwargs['aws_region']))
        self.ecs_client = (
            ecs_client if ecs_client is not None
            else boto3.client("ecs", region_name=kwargs['aws_region']))
        if kwargs.get('assume_role'):
            self.assume_role(kwargs['assume_role'])

    def assume_role(self, role):
        self.sts_client.assume_role(
            RoleArn=role,
            RoleSessionName="Session",
        )
        return "Success"

    def register_task_definition(self):
        definition = ECSTaskDefinition(ecs_client=self.ecs_client, **self.params)
        definition.register()
        return "Success"
