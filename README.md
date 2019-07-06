## 概要
SLACKのメモをドキュメントに起こしてくれるSlack Bot。

### アップロード方法
このリポジトリをzipで固める

lambda関数のzipでアップロードする。

## Slackから送られてくる各種情報のデータ
### Botへのメンション
- 送られたメッセージのID : ['body']['event']['client_msg_id']
- メッセージの本文 : ['body']['event']['text']
- 送信したユーザ : ['body']['event']['user']
- 送信された時刻 : ['body']['event']['ts']
- 送信されたチャンネル : ['body']['event']['channel']

## Lambdaの環境変数
Slackのアクセストークン
- SLACK_BOT_USER_ACCESS_TOKEN
- SLACK_OAUTH_ACCESS_TOKEN