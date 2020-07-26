import pytest
import boto3
from botocore.stub import Stubber

@pytest.fixture(autouse=True)
def sts_stub():
    with Stubber(boto3.client("sts", region_name="us-west-2")) as stubber:
        yield stubber
        stubber.assert_no_pending_responses()


@pytest.fixture(autouse=True)
def ecs_stub():
    with Stubber(boto3.client("ecs", region_name="us-west-2")) as stubber:
        yield stubber
        stubber.assert_no_pending_responses()
