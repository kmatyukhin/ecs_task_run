import click
from .ecs_task_run import ECSTaskRun

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
@click.option(
    "--image", "-i", "image", type=str, required=True,
    help="The image used to start a container",
)
@click.pass_context
def run(*args, **kwargs):
    """Run task in Amazon Elastic Container Service"""
    print(kwargs)
    runner = ECSTaskRun(*args, **kwargs)
