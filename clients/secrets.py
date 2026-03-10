import boto3


class SecretManagerClient:
    def __init__(self, endpoint_url: str):
        self._client = boto3.client("secretsmanager", endpoint_url=endpoint_url)

    @classmethod
    def load(cls, endpoint_url: str) -> "SecretManagerClient":
        return cls(endpoint_url)

    def get_secret(self, secret_id: str) -> str:
        """Fetch secret value. Stub for now."""
        raise NotImplementedError