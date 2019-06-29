import requests
import json

web_url = "http://127.0.0.1:8000"
def test_sms():
    url = "{}/code/".format(web_url)
    data = {
        "mobile":"15138691228"
    }
    res = requests.post(url,json=data)
    print(json.loads(res.text))

def test_register():
    url = "{}/register/".format(web_url)
    data = {
        "mobile":"15138691228",
        "code":"0754",
        "password":"admin123"
    }
    res = requests.post(url,json=data)
    print(json.loads(res.text))


if __name__ == "__main__":
    test_sms()