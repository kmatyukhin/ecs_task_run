import pytest
import boto3
from botocore.stub import Stubber

@pytest.fixture(autouse=True)
def sts_stub():
    with Stubber(boto3.client("sts")) as stubber:
        yield stubber
        stubber.assert_no_pending_responses()
