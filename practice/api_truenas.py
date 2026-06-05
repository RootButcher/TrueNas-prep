from http.client import responses
from unittest import case
from practice.models import Dataset

import requests

class Client:
    _endpoint:str = "/api/v2.0/"
    def __init__(self, host: str, api_key: str,ssl:bool = True, verify_ssl: bool = True):
        self.host = host
        self.ssl = ssl
        self._session = requests.Session()
        self._session.headers["Authorization"] = f"Bearer {api_key}"
        self._session.verify = verify_ssl

    def _make_request(self, method: str, path: str, params: dict = None, data: dict = None)->dict:
        scheme = "https" if self.ssl else "http"
        url = f"{scheme}://{self.host}{self._endpoint}{path}"
        try:
            response = self._session.request(method, url, params=params, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            raise RuntimeError(f"{e.response.status_code} {responses[e.response.status_code]}") from e
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error making request: {e}") from e
    def _get_request(self, path: str)-> dict:
        return self._make_request("GET", path=path)

    def _post_request(self, resource: str, data: dict)-> dict:
        pass

    def _put_request(self, resource: str, data: dict)-> dict:
        pass

    def _patch_request(self, resource: str, data: dict)-> dict:
        pass

    def get_version(self) -> str:
        return self._get_request("system/version_short")

    def list_api_keys(self) -> list[dict]:
        return self._get_request("api_key")

    def get_datasets(self) -> list[Dataset]:
        raw = self._get_request("pool/dataset")
        return [Dataset.model_validate(item) for item in raw]

if __name__ == "__main__":
    from creds import *
    creds = load_secrets()
    client = Client(creds["truenas_host"], creds["truenas_api_key"])
    print(client.get_version())
    print(len(client.get_datasets()))
    #print(client.list_api_keys())