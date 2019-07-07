import json
import threading
import requests
import os
from post_message_to_slack import post_message_to_slack, post_thread_message

def lambda_handler(event, context):
    thread_1 = threading.Thread(target=return_200)
    thread_2 = threading.Thread(target=main_func(event, context))
    return 0

def return_200():
    return 0

# そのメッセージが所属するスレッドをすべて取得
def get_thread_messages(channel, root_ts):
    bot_token = "Bearer {0}".format(os.environ["SLACK_BOT_USER_ACCESS_TOKEN"])
    oauth_token = os.environ["SLACK_OAUTH_ACCESS_TOKEN"]
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    url = "https://slack.com/api/channels.replies?token={0}&channel={1}&thread_ts={2}".format(oauth_token, channel, root_ts)
    res = requests.get(url, headers=headers).json()
    return res

# Slackのユーザ一覧を取得する
def get_slack_user():
    url = "https://slack.com/api/users.list"
    oauth_token = os.environ["SLACK_OAUTH_ACCESS_TOKEN"]

    params = {'token': oauth_token}
    res = requests.get(url, params=params).json()
    return res

def main_func(event, context):
    print(event)
    # Slackからのリクエストがリトライ処理であるかを確認
    if 'X-Slack-Retry-Num' in event['params']['header']:
        print("this is redirect request!.")
        return 0

    post_text = event['body']['event']['text']
    channel = event['body']['event']['channel']
    message_ts = event['body']['event']['ts']

    if 'start_mtg' in post_text:
        message = "MTGを始めるよ！参加する人はjoin、興味がある人はwatchをスレッドに書き込んでね！"
        post_message_to_slack(message, channel)
        return 0

    if 'end_mtg' in post_text:
        thread_root = event['body']['event']['thread_ts']
        thread_messages = get_thread_messages(channel, thread_root)

        p_users = set()
        col_text = ''
        user_ids = []
        user_names = []
        output_text = ""

        slack_users = get_slack_user()

        for slack_user in slack_users["members"]:
            user_ids.append(slack_user['id'])
            user_names.append(slack_user['real_name'])

        # スレッドからユーザが送ったメッセージのIDとテキストを抜き出す
        for thread_message in thread_messages["messages"][1:]:
            # ボットが送ったメッセージを無視
            if "subtype" in thread_message:
                if thread_message["subtype"] == 'bot_message':
                    continue

            # 参加者を抜き出す.ここは重複不可
            if 'join' in thread_message["text"]:
                match_point = user_ids.index(thread_message['user'])
                p_users.add(user_names[match_point])

            # 発言者情報を取得
            if thread_message['user'] in user_ids:
                match_point = user_ids.index(thread_message['user'])
                col_text += "発言者 : {0}\n".format(user_names[match_point])

            # 送信されたメッセージを抜き出す
            col_text += "内容 : {0}\n\n".format(thread_message['text'])

        # 参加者を作成
        output_text += '参加者 : '
        for p_user in p_users:
            output_text += " {} ".format(p_user)

        message = "MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！\n https://www.google.com/"
        print(col_text)
        print(output_text)
        res = post_thread_message(message, channel, message_ts)
        return 0

    message = "そんなコマンドはないよ！以下でヘルプを確認してね"
    post_message_to_slack(message, channel)
    return 0
