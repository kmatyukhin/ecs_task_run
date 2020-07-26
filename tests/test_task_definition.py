import pytest
from ecs_task_run import ECSTaskRun


def test_register_task_definition_function(ecs_stub):
    ecs_stub.add_response(
        'register_task_definition',
        expected_params={
            'family': 'family',
            'containerDefinitions': (),
        },
        service_response={},
    )
    runner = ECSTaskRun(
        ecs_client=ecs_stub.client,
        image='',
        aws_region="us-west-2")
    result = runner.register_task_definition()

    assert result == "Success"
