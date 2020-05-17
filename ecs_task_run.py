#!/usr/bin/env python3
"""Run task in Amazon Elactic Container Service"""
import sys
import click
import boto3


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
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
def main(*args, **kwargs):
    """Run task in Amazon Elastic Container Service"""
    print(kwargs)
    if 'assume_role' in kwargs:
        sts_client = boto3.client("sts", region_name=kwargs['aws_region'])
        assume_role(sts_client, kwargs['assume_role'])


def assume_role(sts_client, role):
    sts_client.assume_role(
        RoleArn=role,
        RoleSessionName="Session",
    )
    return "Success"


def init():
    """Module init function"""
    if __name__ == "__main__":
        sys.exit(main())


init()
