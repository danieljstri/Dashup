from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# Obter o ID da pasta 'dashup'
folder_name = 'dashup'
folder_list = drive.ListFile({'q': "title = '{}' and mimeType = 'application/vnd.google-apps.folder' and trashed=false".format(folder_name)}).GetList()
if folder_list:
    folder_id = folder_list[0]['id']
    # Obter o arquivo 'fluxo.csv' dentro da pasta 'dashup'
    file_name = 'fluxo.csv'
    file_list = drive.ListFile({'q': "'{}' in parents and title = '{}' and trashed=false".format(folder_id, file_name)}).GetList()
    if file_list:
        file_id = file_list[0]['id']
        arquivo = drive.CreateFile({'id': file_id})
        arquivo.GetContentFile(file_name)
    else:
        print('Arquivo não encontrado.')
else:
    print('Pasta não encontrada.')