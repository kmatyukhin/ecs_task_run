import pytest
import mock
from click.testing import CliRunner
from ecs_task_run import main


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
