import boto3

client = boto3.client('sns')

def delete_sqs_subscription():
    response = client.list_subscriptions_by_topic(TopicArn='arn:aws:sns:<region>:<ACCOUNT-NUMBER>:<SNS-TOPIC>')
    while True:
        for subscArn in response['Subscriptions']:
            if "feed-" in subscArn['Endpoint']:
                print("Found endpoint ",subscArn['Endpoint'])
                print("Deleting Subscription",subscArn['SubscriptionArn'])
                response = client.unsubscribe(SubscriptionArn=subscArn['SubscriptionArn'])
                print(response)
        if 'NextToken' in response:
            response = client.list_subscriptions_by_topic(TopicArn='arn:aws:sns:<region>:<ACCOUNT-NUMBER>:<SNS-TOPIC>',  NextToken=response['NextToken'])
        else:
            break

delete_sqs_subscription()
