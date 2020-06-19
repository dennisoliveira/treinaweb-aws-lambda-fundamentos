#!/usr/bin/env sh

set -x

# Create role
aws iam create-role --role-name lambda-tw-node --assume-role-policy-document file://role.json

# Attach Lambda basic execution policy
aws iam attach-role-policy --role-name lambda-tw-node --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

# Package function code in zip
zip function.zip index.js

# Create a Lambda function, referencing the role and the function code package
aws lambda create-function --function-name tw-node \
  --zip-file fileb://function.zip --handler index.handler --runtime nodejs12.x \
  --role arn:aws:iam::123456789012:role/lambda-tw-node
