from tornado.web import url

from apps.message.handler import *

urlpattern = (
    url("/messages/",MessageHandler),

)