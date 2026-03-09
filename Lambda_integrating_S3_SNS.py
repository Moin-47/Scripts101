import boto3
import json

def lambda_handler(event, context):
    
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    print("New file uploaded: " + object_key + " in bucket: " + bucket_name)
    
    sns = boto3.client('sns', region_name='paste your region here')
    
    topic_arn = 'Paste:your:SNS:Topic:ARN:Here'
    
    message = "A new file has been uploaded!\n\nBucket: " + bucket_name + "\nFile: " + object_key
    
    response = sns.publish(
        TopicArn=topic_arn,
        Subject='New File Uploaded to S3',
        Message=message
    )
    
    print("SNS notification sent: " + response['MessageId'])
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully!')
    }