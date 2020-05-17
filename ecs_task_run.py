#!/usr/bin/env python3
"""Run task in Amazon Elactic Container Service"""
import sys
import click


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.pass_context
@click.option(
    "--cluster", "-c", "cluster_name", type=str, required=True,
    help="Name of ECS cluster",
)
@click.option(
    "--region", "-r", "region", type=str, required=True,
    help="AWS region",
)
def main(**kwargs):
    """Run task in Amazon Elastic Container Service"""

def init():
    """Module init function"""
    if __name__ == "__main__":
        sys.exit(main())


init()
