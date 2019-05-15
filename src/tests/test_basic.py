from .api_examples import *


def test_pull_request_merged_false(client):
    rv = client.post("/", data=pull_request_webhook_event())
    assert rv.data == b'Exit'


def test_pull_request_merged(client):
    rv = client.post("/", data=pull_request_master_merged())
    assert rv.data == b'OK'
