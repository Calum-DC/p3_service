import os
import pytest
import boto3
from moto import mock_aws
from main import app

REGION='us-east-1'
AWS_REGION='us-east-1'
@pytest.fixture(scope='function')
def aws_credentials():
    """Mock AWS credentials for moto moto"""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_REGION'] = REGION  
    os.environ['jira_client'] = 'testing'

@pytest.fixture
def client():
    """test client."""
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='function')
def sqs_client(aws_credentials):
    with mock_aws():
        yield boto3.client('sqs', region_name=REGION)

