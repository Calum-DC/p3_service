import boto3
import json
import os

from flask import Flask, jsonify
from dotenv import load_dotenv


app = Flask(__name__)

# Load environment variables
load_dotenv()
sqs_client = boto3.client('sqs', region_name=os.getenv('AWS_REGION'))
ses_client = boto3.client('ses', region_name=os.getenv('AWS_REGION'))


QUEUE_URL = os.getenv('SQS_P3_URL')
SES_EMAIL = os.getenv('SES_EMAIL')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')


def process_sqs_p3_message():

    title = "Broken frontend"
    description = "The frontend of the website is broken"

    email_template = f"Hello,\n\nPlease see below the following high priority bug report:\n\nTitle: {title}\n\nDescription: {description}"

    ses_client.send_email(
        Source=SES_EMAIL,
        Destination = {'ToAddresses': [RECIPIENT_EMAIL]},
        Message = {
            'Subject': {
                'Data': f"High Priority Bug: {title}"
            },
            'Body': {
                'Text':{
                    'Data': email_template
                }
            }
        }
    )


if __name__ == '__main__':
    process_sqs_p3_message()
    app.run(debug=False, port=5003)