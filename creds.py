from sopsy import Sops
from pathlib import Path

SECRETS_FILE = Path(__file__).parent / "truenas_api.sops.yaml"
def load_secrets():
    sops = Sops(SECRETS_FILE)
    return sops.decrypt()

def get_api_key():
    return load_secrets()["truenas_api_key"]

def get_host():
    return load_secrets()["truenas_host"]

if __name__ == "__main__":
    print(load_secrets())