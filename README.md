## 概要
SLACKのメモをドキュメントに起こしてくれるSlack Bot。
lambdaで作成しようと思ったが、Google Drive Apiの仕様上難しいので、django-rest-apiで作成する

## Botの返答
- start_mtg : MTGを始めるよ！スレッドに```@PUTO title MTGのタイトル```を入力してね！
- title : タイトルを保存したよ！このＭＴＧに参加する人はjoin、興味がある人はwatchをスレッドに書き込んでね！
- end_mtg : MTGを終了したよ！このスレッドの内容は以下のリンクに書き込んでおいたよ！
コマンドなし
そんなコマンドはないよ！以下でヘルプを確認してね

英語ver
- start_mtg: Starting the meeting! Type `@PUTO title <meeting_title>` in the thread!
- title: Title saved successfully! Type `join` to join the meeting, or `watch` if you are interested in the meeting!
- end_mtg: The meeting has ended! See the contents of this thread in the following link!
not found
I cant't find command...\n
Check `@PUTO help` command.

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
- テキスト群 : ['messages'][0]['replies']['']
- その詳細 : ['messages'][X]['text']
- 送られたメッセージのタイプ : ['messages'][X]['subtype'] or ['messages'][X]['type']
bot_messageをはじく
subtypeはbotだけ
- それを送ったユーザID : ['messages'][X]['user']

## ユーザ一覧を取得する
GETでとれる。スコープ必要。Botもとれる
- ユーザID : ['members'][X]['id']
- ユーザ名 : ['members'][X]['real_name']

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

## Googleドライブの各種
https://qiita.com/akabei/items/f25e4f79dd7c2f754f0e
これにはGCP側で受け取り関数を作成する必要があるので、それを設定する。

まず新しいプロジェクトを作成する。
OAuthIDを発行する。

Drive APIを有効化して、認証情報を作成する。
### ファイルアップロード
参考
https://news.mynavi.jp/article/zeropython-16/
以下のパッケージが必要
```
google-api-python-client PyDrive
```

ローカルにインストール
```
pip install google-api-python-client PyDrive -t .
```

Driveへの初回書き込みは認証が必要なので、ローカルで実行してから

特定のフォルダ配下に書き込むためには、フォルダのIDが必要。

## 認証プロセスを無効化する

## ファイルとフォルダを検索する
フォルダはランダムなIDで管理されている。

## Lambdaの環境変数
Slackのアクセストークン
- SLACK_BOT_USER_ACCESS_TOKEN
- SLACK_OAUTH_ACCESS_TOKEN

## 参考文献
https://qiita.com/gureta/items/879eef81055921f845aa
https://admarimoin.hatenablog.com/entry/2018/05/07/200939
https://news.mynavi.jp/article/zeropython-16/
https://codeday.me/jp/qa/20190107/136715.html

トークン切れ
<!-- def save_text_file(folder_id, text, title="title_not_found"): -->
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)

    file_name = "test.txt"
    f = drive.CreateFile({'title': file_name})
    f.SetContentString('test')
    f.Upload()


プレゼン
@PUTO start_
Planning for the next season