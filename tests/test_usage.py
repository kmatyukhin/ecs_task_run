import pytest
from click.testing import CliRunner
from ecs_task_run import run, ECSTaskRun


def test_help():
    runner = CliRunner()
    result = runner.invoke(run, ['--help'])

    assert "Usage" in result.output
    assert "Error" not in result.output


def test_help_short():
    runner = CliRunner()
    result = runner.invoke(run, ['-h'])

    assert "Usage" in result.output
    assert "Error" not in result.output


def test_required_options():
    runner = CliRunner()
    result = runner.invoke(run, [])

    assert "Usage" in result.output
    assert "Error" in result.output


def test_assume_role_option():
    runner = CliRunner()
    result = runner.invoke(run, [
        "--cluster=1",
        "--region=1",
        "--image=1",
        "--assume-role=test-role"
    ])

    assert True


def test_image_option():
    runner = CliRunner()
    result = runner.invoke(run, [
        "--cluster=1",
        "--region=1",
        "--image=helo-world"
    ])

    assert True


def test_assume_role_function(sts_stub):
    sts_stub.add_response(
        'assume_role',
        expected_params={
            'RoleArn': 'arn:::00000000000:test-role',
            'RoleSessionName': 'Session',
        },
        service_response={},
    )
    runner = ECSTaskRun(
        sts_client=sts_stub.client,
        aws_region="us-west-2")
    result = runner.assume_role(
        role='arn:::00000000000:test-role')

    assert result == "Success"
