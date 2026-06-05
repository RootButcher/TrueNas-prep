import pytest
from practice.api_truenas import Client
from creds import *
1
@pytest.fixture(scope="session")
def client():
    secrets = load_secrets()
    return Client(secrets["truenas_host"], secrets["truenas_api_key"])

@pytest.fixture(scope="session")
def datasets(client):
    return client.get_datasets()

def test_consistent_datasets(client, datasets):
    assert len(datasets) == len(client.get_datasets())
    assert datasets == client.get_datasets()

def test_list_datasets(datasets):
    assert len(datasets) > 0

def test_pool_name_consistency(datasets):
    for d in datasets:
        assert d.id.startswith(d.pool)

def test_dataset_ids_are_unique(datasets):
    ids = [d.id for d in datasets]
    assert len(ids) == len(set(ids))


