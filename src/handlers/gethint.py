import json
import os

import boto3

HINTS_DELIMITER = "##"

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
    hints_unjoined = response['Item']['hint']
    hints = hints_unjoined.split(HINTS_DELIMITER)

    print("Sending back hints:")
    print(hints)

    body = {'hints': hints}

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
        },
        'body': json.dumps(body),
    }

