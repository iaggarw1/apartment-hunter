from clients.dynamo import DynamoClient
from clients.redis import RedisClient
from clients.secrets import SecretManagerClient


class Agent:
    def __init__(self, db: DynamoClient, redis: RedisClient, secrets: SecretManagerClient):
        self.db = db
        self.redis = redis
        self.secrets = secrets

    @classmethod
    def start(
        cls,
        db: DynamoClient,
        redis: RedisClient,
        secrets: SecretManagerClient,
    ) -> "Agent":
        """Create and return an agent instance. Entry point for agentic workflow."""
        return cls(db=db, redis=redis, secrets=secrets)