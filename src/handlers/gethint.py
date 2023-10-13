import json
import os

import boto3

def handler(event, context):
    "Return AWS lambda response OKAY"

    problem_id = event['queryStringParameters']['problemId']

    print("Querying for problem id: " + problem_id + "\n")

    # Access dynamo db with name
    name = os.environ['TABLE_NAME']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(name)
    response = table.get_item(
        Key={
            'prob_id': problem_id,
        }
    )

    # Get hint field from first item
    hint = response['Item']['hint']
    print("GOT HINT:\n" + hint)

    body = {'hint': hint}

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
        },
        'body': json.dumps(body),
    }

