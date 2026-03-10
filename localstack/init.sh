#!/bin/bash
set -e
echo "######### Starting LocalStack Resources ##########"

awslocal dynamodb create-table \
    --table-name profiles \
    --attribute-definitions \
        AttributeName=user_id,AttributeType=S \
        AttributeName=name,AttributeType=S \
    --key-schema \
        AttributeName=user_id,KeyType=HASH \
        AttributeName=name,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST

echo "######### LocalStack init complete ##########"