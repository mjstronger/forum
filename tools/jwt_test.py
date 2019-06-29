from datetime import datetime

import jwt
from XmForm.settings import settings

current_time = datetime.utcnow()

data = jwt.encode({
    "name":"xming",
    "id":1,
    "exp":current_time
},"adc").decode("utf8")

import time
time.sleep(2)

send_data = jwt.decode(data,settings["secret_key"],leeway=1,options={"verify_exp":False})

print(send_data)