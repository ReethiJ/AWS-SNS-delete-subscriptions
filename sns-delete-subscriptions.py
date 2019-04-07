import boto3

client = boto3.client('sns')

def delete_sqs_subscription():
    sns_list_response = client.list_subscriptions_by_topic(TopicArn='arn:aws:sns:<region>:<ACCOUNT-NUMBER>:<SNS-TOPIC>')
    while True:
        for subscArn in sns_list_response['Subscriptions']:
            if "<SOME-PREFIX>" in subscArn['Endpoint']:
                print("Found endpoint ",subscArn['Endpoint'])
                print("Deleting Subscription",subscArn['SubscriptionArn'])
                unsubs_response = client.unsubscribe(SubscriptionArn=subscArn['SubscriptionArn'])
                print(unsubs_response)
        if 'NextToken' in sns_list_response:
            sns_list_response = client.list_subscriptions_by_topic(TopicArn='arn:aws:sns:<region>:<ACCOUNT-NUMBER>:<SNS-TOPIC>',  NextToken=sns_list_response['NextToken'])
        else:
            break

delete_sqs_subscription()
