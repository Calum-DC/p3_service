import json
import pytest
import os


@pytest.fixture(scope='function')
def queue_url_mock(sqs_client):
    '''create mock queues for use in the p1,2, and 3 tests'''
    queue_urls = {
        '1': sqs_client.create_queue(QueueName='P1Queue')['QueueUrl'],
        '2': sqs_client.create_queue(QueueName='P2Queue')['QueueUrl'],
        '3': sqs_client.create_queue(QueueName='P3Queue')['QueueUrl']
    }
    return queue_urls


def test_health_check(client):
    """Test to ensure the /health route is working."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
