# Eventが発生した部屋に対して、メッセージを投げる関数
import json
import os
import requests

# イベントが起こった部屋にパブリックなリプライを返す
def post_message_to_slack(message: str, channel: str):
    # Slackのchat.postMessage APIを利用して投稿する

    bot_token = "Bearer {0}".format(os.environ["SLACK_BOT_USER_ACCESS_TOKEN"])
    oauth_token = os.environ["SLACK_OAUTH_ACCESS_TOKEN"]

    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": bot_token
    }
    data = {
        "token": oauth_token,
        "channel": channel,
        "text": message
    }

    res = requests.post(url, data=json.dumps(data).encode("utf-8"), headers=headers)
    return res

# イベントが起こった部屋にその人だけにしか見えないメンションを返す
def post_personal_message_to_slack(message: str, channel: str, user: str):
    # Slackのchat.postMessage APIを利用して投稿する

    bot_token = "Bearer {0}".format(os.environ["SLACK_BOT_USER_ACCESS_TOKEN"])
    oauth_token = os.environ["SLACK_OAUTH_ACCESS_TOKEN"]

    url = "https://slack.com/api/chat.postEphemeral"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": bot_token
    }

    data = {
        "token": oauth_token,
        "channel": channel,
        "text": message,
        "user": user
    }

    requests.post(url, data=json.dumps(data).encode("utf-8"), headers=headers)

    return

# スレッドで返信する
def post_thread_message(message, channel, ts):
    print('call post_thread_message')
    bot_token = "Bearer {0}".format(os.environ["SLACK_BOT_USER_ACCESS_TOKEN"])
    oauth_token = os.environ["SLACK_OAUTH_ACCESS_TOKEN"]

    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": bot_token
    }

    data = {
        "token": oauth_token,
        "channel": channel,
        "text": message,
        "thread_ts": ts
    }

    res = requests.post(url, data=json.dumps(data).encode("utf-8"), headers=headers)
    return res
