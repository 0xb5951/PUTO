import json
from post_message_to_slack import post_message_to_slack

def lambda_handler(event, context):
    print(event)

    channel = event['body']['event']['channel']
    message = "MTGを始めるよ！参加する人はjoin、興味がある人はwatchをスレッドに書き込んでね！"
    post_message_to_slack(message, channel)
    return 0
