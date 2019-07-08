from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# 指定された場所にテキストファイルを保存する
gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)

file_name = "test.txt"
f = drive.CreateFile({'title': file_name})
f.SetContentString('test')
f.Upload()
