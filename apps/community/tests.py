import json
from datetime import datetime
import requests
import jwt

current_time = datetime.utcnow()

from XmForm.settings import settings

web_site_url = "http://127.0.0.1:8000"
data = jwt.encode({
    "name":"xming",
    "id":1,
    "exp":current_time
},settings["secret_key"]).decode("utf8")
headers ={
        "tsessionid":data
    }
def new_group():
    files = {
        "front_image":open("C:/Users/zjm/Pictures/48313a3eb80e7becfab40fb1222eb9389b506b21.jpg","rb")
    }
    data = {
        "name": "学前教育交流角",
        "desc": "这里是学前教育的交流中心，大家有什么问题可以一起来交流讨论！欢迎大家的加入！",
        "notice": "这里是学前教育的交流中心，大家有什么问题可以一起来交流讨论！欢迎大家的加入！",
        "category": "教育同盟"
    }
    res = requests.post("{}/groups/".format(web_site_url),headers=headers, data = data,files=files)
    print(res.status_code)
    print(json.loads(res.text))
def apply_group(group_id,apply_reason):
    data={
        "apply_reason":apply_reason,
    }
    res = requests.post("{}/group/{}/members/".format(web_site_url,group_id),headers=headers,json=data)

    print(res.status_code)
    print(json.loads(res.text))

def get_applys():
    res = requests.get("{}/applys/".format(web_site_url),headers=headers)
    print(res.status_code)
    print(json.loads(res.text))

if __name__ == "__main__":
    #新建小组
    # apply_group(1,"test")
    get_applys()