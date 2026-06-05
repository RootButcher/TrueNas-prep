import pytest
from practice.api_truenas import Client
from creds import *
1
@pytest.fixture(scope="session")
def client():
    secrets = load_secrets()
    return Client(secrets["truenas_host"], secrets["truenas_api_key"])

def test_list_datasets(client):
    datasets = client.get_datasets()
    assert len(datasets) > 0

def test_pool_name_consistency(client):
    for d in client.get_datasets():
        assert d.id.startswith(d.pool)

def test_dataset_ids_are_unique(client):
    datasets = client.get_datasets()
    ids = [d.id for d in datasets]
    assert len(ids) == len(set(ids))


