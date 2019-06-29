import os
import uuid
import json

from XmForm.handler import RedisHandler
from apps.utils.Xmform_decorators import authenticated_async
from apps.message.models import Message
from apps.users.models import User



class MessageHandler(RedisHandler):
    @authenticated_async
    async def get(self, *args, **kwargs):
        # 获取当前用户的消息
        re_data = []

        type_list = self.get_query_arguments("message_type", [])
        if type_list:
            message_query = Message.filter(Message.receiver_id == self.current_user.id,
                                           Message.message_type.in_(type_list))
        else:
            message_query = Message.filter(Message.receiver_id == self.current_user.id)
        messages = await self.application.objects.execute(message_query)
        for message in messages:
            sender = await self.application.objects.get(User, id=message.sender_id)
            re_data.append({
                "sender": {
                    "id": sender.id,
                    "nick_name": sender.nick_name,
                    "head_url": "media/" + sender.head_url
                },
                "message": message.message,
                "message_type": message.message_type,
                "parent_content": message.parent_content,
                "add_time": message.add_time.strftime("%Y-%m-%d %H:%M:%S")
            })
        self.finish(json.dumps(re_data))
