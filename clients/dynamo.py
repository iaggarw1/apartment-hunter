import boto3

from core.models.profile import Profile


class DynamoClient:
    def __init__(self, endpoint_url: str):
        self._client = boto3.client("dynamodb", endpoint_url=endpoint_url)

    @classmethod
    def load(cls, endpoint_url: str) -> "DynamoClient":
        return cls(endpoint_url)

    def put(self, table: str, profile: Profile) -> None:
        """Persist profile to DynamoDB. Stub for now."""
        pass