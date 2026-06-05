import os
from pathlib import Path

SECRETS_FILE = Path(__file__).parent / "truenas_api.sops.yaml"

ENV_MAP = {
    "truenas_host": "TRUENAS_HOST",
    "truenas_api_key": "TRUENAS_API_KEY",
}

class MissingSecretError(RuntimeError):
    pass

def load_secrets():
    out = {}
    for key, env_var in ENV_MAP.items():
        val = os.environ.get(env_var)
        if val is None:
            try:
                from sopsy import Sops
            except ImportError:
                raise MissingSecretError(
                    f"env var {env_var} is not set and sopsy is unavailable"
                )
            val = Sops(SECRETS_FILE).get(key)
        out[key] = val
    return out

def get_api_key():
    return load_secrets()["truenas_api_key"]

def get_host():
    return load_secrets()["truenas_host"]

if __name__ == "__main__":
    print(load_secrets())