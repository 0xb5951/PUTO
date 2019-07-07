from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



# 指定された場所にテキストファイルを保存する
def save_text_file(folder_id, title, text):
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)

    file_name = title + ".txt"

    f = drive.CreateFile({'title': file_name,
                          'parents': [{'kind': 'drive#fileLink', 'id': folder_id}]})
    f.SetContentString(text)
    f.Upload()

folder_id = '1S1Pv5OdU55vQLpdFkaNh-J7GxDjSQh2-'
save_text_file(folder_id, 'test', 'test')
