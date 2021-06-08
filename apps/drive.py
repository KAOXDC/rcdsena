import requests
import json 
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


saved_image_url='ejemplo.png'
def save_image_in_drive(file_name):

    print (str(BASE_DIR) + '/media/samples/' + file_name)
    
    headers = {
        'Authorization': "Bearer ya29.a0AfH6SMALsnQ3cN9oNvDUtFpuhN1gE5bkV9cyGwHoSXmlY1eRL6FNKQcfLBanweTGUfVKmtQXUFNNJItBKd48ZQrmaCK0Lkk4nIsjxgrDRJDN1FScrZQTbTE8CnxExC9QgxAHhLVQj6qXYFayzs-W7gK5qOJf"
    }
    para = {
        "name": file_name,
        'parents': ['19BISbpuN3KJ4Y4S-GwUqtF9rk7hzT70b'],
    }
    
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open('C:/Users/Diego/Desktop/Proyectos/rcd' + '/media/samples/' + file_name, 'rb'),      #open('././'+saved_image_url, "rb") #./imagen.png
    }

    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files,
    )
    print (r.text)
    res = json.loads(r.text)
    #new_image_url = 'https://drive.google.com/file/d/'+ res['id'] + '/view?usp=sharing'
    return res['id']

# https://drive.google.com/file/d/17ArDM_ue-yDUtF98VRidWIF-vy61Ovkj/view?usp=sharing
# IMAGE ID= "17ArDM_ue-yDUtF98VRidWIF-vy61Ovkj"
# 

# print(save_image_in_drive(saved_image_url))
