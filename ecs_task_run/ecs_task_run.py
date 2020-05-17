"""Run task in Amazon Elactic Container Service"""
import sys
import boto3


class ECSTaskRun:
    params = {}
    def __init__(self, *args, sts_client=None, **kwargs):
        self.params = kwargs
        self.sts_client = (
            sts_client if sts_client is not None
            else boto3.client("sts", region_name=kwargs['aws_region']))
        if kwargs.get('assume_role'):
            self.assume_role(kwargs['assume_role'])

    def assume_role(self, role):
        self.sts_client.assume_role(
            RoleArn=role,
            RoleSessionName="Session",
        )
        return "Success"
