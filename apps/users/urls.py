from tornado.web import url
from apps.users.handler import *


urlpattern = (
    url("/code/",SmsHandler),
    url("/register/",RegisterHandler),
    url("/login/",LoginHandler),
    url("/info/",ProfileHandler),
    url("/headimages/",HeadImagesHandler),
    url("/password/",ChanegPasswordHandler),
)