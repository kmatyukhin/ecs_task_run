#!/usr/bin/env python3
import sys
import click

@click.command()
@click.pass_context
def main(ctx, option=None):
    """Run task in Amazon Elastic Container Service"""
    if not option:
        click.echo(ctx.get_help())
        ctx.exit()


def init():
    if __name__ == "__main__":
        sys.exit(main())


init()
