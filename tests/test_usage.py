import pytest
import mock
from click.testing import CliRunner
from ecs_task_run import main, assume_role


def test_init():
    import ecs_task_run
    with mock.patch.object(ecs_task_run, "main", return_value=42):
        with mock.patch.object(ecs_task_run, "__name__", "__main__"):
            with mock.patch.object(ecs_task_run.sys,'exit') as mock_exit:
                ecs_task_run.init()

                assert mock_exit.call_args[0][0] == 42


def test_help():
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])

    assert "Usage" in result.output
    assert "Error" not in result.output


def test_help_short():
    runner = CliRunner()
    result = runner.invoke(main, ['-h'])

    assert "Usage" in result.output
    assert "Error" not in result.output


def test_required_options():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert "Usage" in result.output
    assert "Error" in result.output


def test_assume_role_option():
    runner = CliRunner()
    result = runner.invoke(main, [
        "--cluster=1",
        "--region=1",
        "--assume-role=test-role"
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

    result = assume_role(sts_stub.client, role='arn:::00000000000:test-role')

    assert result == "Success"
