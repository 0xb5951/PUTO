## 概要
SLACKのメモをドキュメントに起こしてくれるSlack Bot。

### アップロード方法
このリポジトリをzipで固める

lambda関数のzipでアップロードする。

## Slackから送られてくる各種情報のデータ### Botへのメンション
- 送られたメッセージのID : ['body']['event']['client_msg_id']
- メッセージの本文 : ['body']['event']['text']
- 送信したユーザ : ['body']['event']['user']
- 送信された時刻 : ['body']['event']['ts']
- 送信されたチャンネル : ['body']['event']['channel']
- そのメッセージの根スレッド : ['body']['event']['thread_ts']

### 全体
- メッセージのタイプ : ['body']['event']['type']

### スレッドメッセージ
GETでとれる。
- テキスト群 : [0]['messages']['replies']['']
- その詳細 : [X]['text']
- 送られたメッセージのタイプ : [X]['subtype']
bot_messageをはじく
- それを送ったユーザ : [X]['user']

## Slackのスレッドもろもろ
### スレッドに返信するには
Slackのスレッドに変身するには、チャンネル名とそのメッセージのタイムスタンプが必要
それさえ指定すれば、スレッドで返信できる。

### そのメッセージが所属するスレッドをすべて取得する
以下のAPIを使えば可能
https://api.slack.com/methods/channels.replies/test

`channels.history`の権限が必要。
以下の形式でGETリクエストを投げる。
```
https://slack.com/api/channels.replies?token=SLACKトークン&channel=チャンネル名&thread_ts=メッセージのタイムスタンプ
```
スレッドが開始したメッセージのタイムスタンプを入力する必要がある。


## Lambdaの環境変数
Slackのアクセストークン
- SLACK_BOT_USER_ACCESS_TOKEN
- SLACK_OAUTH_ACCESS_TOKEN

## 参考文献
https://qiita.com/gureta/items/879eef81055921f845aa



{
    "messages": [
        {
            "client_msg_id": "763fb27f-9f6b-4a46-af2c-c45ce81a577e",
            "type": "message",
            "text": "<@UL8FXT8QN> test",
            "user": "UL6BCLWE4",
            "ts": "1562399355.021000",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "reply_count": 32,
            "reply_users_count": 2,
            "latest_reply": "1562452701.000100",
            "reply_users": [
                "BL8792TL7",
                "UL6BCLWE4"
            ],
            "replies": [
                {
                    "user": "BL8792TL7",
                    "ts": "1562399357.021100"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562399437.021400"
                },
                {
                    "user": "BL8792TL7",
                    "ts": "1562399440.021600"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562400804.025700"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562400839.026000"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562400897.026200"
                },
                {
                    "user": "BL8792TL7",
                    "ts": "1562400899.026400"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562401043.026600"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562401140.026800"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562401197.027000"
                },
                {
                    "user": "BL8792TL7",
                    "ts": "1562401200.027200"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562401295.027400"
                },
                {
                    "user": "BL8792TL7",
                    "ts": "1562401299.027600"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562401634.027800"
                },
                {
                    "user": "BL8792TL7",
                    "ts": "1562401637.028000"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562401985.028200"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562402029.028400"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562402245.028600"
                },
                {
                    "user": "BL8792TL7",
                    "ts": "1562402248.028800"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562402511.029000"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562402788.029200"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562402891.029400"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562402960.029600"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562403093.029800"
                },
                {
                    "user": "BL8792TL7",
                    "ts": "1562403096.030000"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562403192.030200"
                },
                {
                    "user": "BL8792TL7",
                    "ts": "1562403195.030400"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562403394.030600"
                },
                {
                    "user": "BL8792TL7",
                    "ts": "1562403398.030800"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562403544.031000"
                },
                {
                    "user": "BL8792TL7",
                    "ts": "1562403547.031200"
                },
                {
                    "user": "UL6BCLWE4",
                    "ts": "1562452701.000100"
                }
            ],
            "subscribed": true,
            "last_read": "1562452701.000100"
        },
        {
            "type": "message",
            "subtype": "bot_message",
            "text": "スレッドへの返信テスト",
            "ts": "1562399357.021100",
            "username": "PUTO",
            "bot_id": "BL8792TL7",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "b92c91e0-a576-41d1-810d-24adb09854a8",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562399437.021400",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "type": "message",
            "subtype": "bot_message",
            "text": "MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！\n <https://www.google.com/>",
            "ts": "1562399440.021600",
            "username": "PUTO",
            "bot_id": "BL8792TL7",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "1308f5ce-ebf5-4fb1-809e-a75de3d856a5",
            "type": "message",
            "text": "<@UL8FXT8QN> enc_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562400804.025700",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "5525987f-c42b-483c-a535-9fcfda85406f",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562400839.026000",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "1bf5821e-664c-43ad-953f-376b8af6627a",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562400897.026200",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "type": "message",
            "subtype": "bot_message",
            "text": "MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！\n <https://www.google.com/>",
            "ts": "1562400899.026400",
            "username": "PUTO",
            "bot_id": "BL8792TL7",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "4e22d8ca-8c7d-44ae-bbeb-4d2421ed65fa",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562401043.026600",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "bd96bba0-67b5-4b35-bf18-c0f21170c362",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562401140.026800",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "81446644-acac-4eb7-ac7e-8351881480f1",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562401197.027000",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "type": "message",
            "subtype": "bot_message",
            "text": "MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！\n <https://www.google.com/>",
            "ts": "1562401200.027200",
            "username": "PUTO",
            "bot_id": "BL8792TL7",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "568fc8f5-cdea-45eb-871e-dda7c71e9048",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562401295.027400",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "type": "message",
            "subtype": "bot_message",
            "text": "MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！\n <https://www.google.com/>",
            "ts": "1562401299.027600",
            "username": "PUTO",
            "bot_id": "BL8792TL7",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "6d5e1da3-be94-4551-a924-fda0a7e8a85e",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562401634.027800",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "type": "message",
            "subtype": "bot_message",
            "text": "MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！\n <https://www.google.com/>",
            "ts": "1562401637.028000",
            "username": "PUTO",
            "bot_id": "BL8792TL7",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "fc2555a5-74cd-4116-bf94-eaee19462617",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562401985.028200",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "9275b12d-fa38-4315-84f2-d5e41f1abfa7",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562402029.028400",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "583977d7-490c-4761-8155-0ec3c037daed",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562402245.028600",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "type": "message",
            "subtype": "bot_message",
            "text": "MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！\n <https://www.google.com/>",
            "ts": "1562402248.028800",
            "username": "PUTO",
            "bot_id": "BL8792TL7",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "3182df4f-a047-4bd4-ab55-88c7131f7b88",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562402511.029000",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "140e8506-bd4f-4054-8a73-8b249dacdc39",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562402788.029200",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "ba33afe4-331e-49ff-8914-8651b7e06cd0",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562402891.029400",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "cdf9f679-56ab-442f-b2fb-ac1ea64a421d",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562402960.029600",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "b871b815-7e58-4c1a-aa90-7baa0d347e71",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562403093.029800",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "type": "message",
            "subtype": "bot_message",
            "text": "MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！\n <https://www.google.com/>",
            "ts": "1562403096.030000",
            "username": "PUTO",
            "bot_id": "BL8792TL7",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "aeb52b08-dee1-45a6-95a9-f2446a678afb",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562403192.030200",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "type": "message",
            "subtype": "bot_message",
            "text": "MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！\n <https://www.google.com/>",
            "ts": "1562403195.030400",
            "username": "PUTO",
            "bot_id": "BL8792TL7",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "0c8c0409-3ac9-47bc-aab8-0846d4cbcf15",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562403394.030600",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "type": "message",
            "subtype": "bot_message",
            "text": "MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！\n <https://www.google.com/>",
            "ts": "1562403398.030800",
            "username": "PUTO",
            "bot_id": "BL8792TL7",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "0580e55f-5222-4bc0-9d6e-245bb7ae175c",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562403544.031000",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "type": "message",
            "subtype": "bot_message",
            "text": "MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！\n <https://www.google.com/>",
            "ts": "1562403547.031200",
            "username": "PUTO",
            "bot_id": "BL8792TL7",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        },
        {
            "client_msg_id": "8ba5add7-5ddd-46b1-bd1d-06c0617bd43f",
            "type": "message",
            "text": "<@UL8FXT8QN> end_mtg",
            "user": "UL6BCLWE4",
            "ts": "1562452701.000100",
            "team": "TL6BQ5USH",
            "thread_ts": "1562399355.021000",
            "parent_user_id": "UL6BCLWE4"
        }
    ],
    "has_more": false,
    "ok": true
}