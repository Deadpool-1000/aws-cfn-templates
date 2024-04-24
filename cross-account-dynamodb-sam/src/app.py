import boto3


def lambda_handler(event, context):
    # Assume the cross-account role in Account-B
    print("trying....")
    raise Exception
    sts_connection = boto3.client('sts')
    acct_b = sts_connection.assume_role(
        RoleArn="arn:aws:iam::654654393019:role/LambdaDynamoDBcrossAccountRole",
        RoleSessionName="cross_acct_lambda"
    )

    ACCESS_KEY = acct_b['Credentials']['AccessKeyId']
    SECRET_KEY = acct_b['Credentials']['SecretAccessKey']
    SESSION_TOKEN = acct_b['Credentials']['SessionToken']

    dynamo_client = boto3.client(
        'dynamodb',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN,
    )


    table_name = "ECommerceTable"
    if 'Records' in event:
        if len(event['Records']) > 0:
            if 'dynamodb' in event['Records'][0]:
                if 'NewImage' in event['Records'][0]['dynamodb']:
                    item = event['Records'][0]['dynamodb']['NewImage']
                    dynamo_client.put_item(
                        TableName=table_name,
                        Item=item
                    )
        