"""
Backend gateway: agentic workflow and microservice orchestration.

Not exposed to clients. The API layer (main.py) calls into the gateway
when it needs agent-driven or multi-service work.
"""
import os

from clients.dynamo import DynamoClient
from clients.redis import RedisClient
from clients.secrets import SecretManagerClient
from core.models.agent import Agent


def launch() -> Agent:
    """Bootstrap gateway: connect to DynamoDB, Redis, Secrets; return running agent."""
    db = DynamoClient.load(os.environ["DYNAMO"])
    redis = RedisClient.load(os.environ["REDIS"])
    secret = SecretManagerClient.load(os.environ["SECRETS"])
    return Agent.start(db=db, redis=redis, secrets=secret)