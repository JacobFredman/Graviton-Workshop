from flask import jsonify
import random
import string
import boto3
table_name = "GravitonWorkshopCreateDdbCdkStack-GravitonWorkshopDdbUrlsTableF0951F41-9D16PC6I65SY"


def retrive_from_dynamo(short_url):
    # Create a DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Specify the table
    table = dynamodb.Table(table_name)
    try: 
        # Get item from the table
        response = table.get_item(
            Key={
                'short_url': short_url
            }
        )
        print('retrive_from_dynamo')
        return response['Item']
    except Exception as e:
        return str(e)


# create a function to shortening url
def create_short_url(url):
    try:
        # create a random string of length 10
        letters = string.ascii_lowercase
        short_url = ''.join(random.choice(letters) for i in range(10))
        save_in_dynamo(short_url, url)
        # append the random string generated to the url
        return jsonify({'short_url':short_url}) 
    except Exception as e:
        return str(e)
    

def save_in_dynamo(short_url, original_url):
    # Create a DynamoDB resource
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Specify the table
    table = dynamodb.Table(table_name)
    try: 
        # Put item in the table
        response = table.put_item(
        Item={
                'short_url': short_url,
                'url': original_url
            }
        )
        print('save_in_dynamo')
    except Exception as e:
        return str(e)

    return response

