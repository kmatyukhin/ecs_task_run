#!/usr/bin/env python3
"""Run task in Amazon Elactic Container Service"""
import sys
import click
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


@click.command(
    context_settings=dict(help_option_names=['-h', '--help'])
)
@click.option(
    "--cluster", "-c", "cluster_name", type=str, required=True,
    help="Name of ECS cluster",
)
@click.option(
    "--region", "-r", "aws_region", type=str, required=True,
    help="AWS region",
)
@click.option(
    "--assume-role", "-a", "assume_role", type=str,
    help="Assume IAM role before run the task",
)
@click.pass_context
def main(*args, **kwargs):
    """Run task in Amazon Elastic Container Service"""
    print(kwargs)
    runner = ECSTaskRun(*args, **kwargs)

def init():
    """Module init function"""
    if __name__ == "__main__":
        sys.exit(main())


init()
