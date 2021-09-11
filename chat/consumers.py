from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import ChatRoom , Privatenotifications

from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

class ChatConsumer(WebsocketConsumer):

    
    

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        

        # self.send(text_data=json.dumps({'status' : 'connected'}))


    
    

    def receive(self , text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        room = text_data_json['room']
        sender = text_data_json['sender']
        receiver = text_data_json['receiver']
        link = text_data_json['link']
        img = text_data_json['img']

        notifications = Privatenotifications.objects.filter(sender = sender, receiver = receiver , seen = False)
        
        if not notifications:

            Privatenotifications.objects.create(sender = sender, receiver = receiver)

        obj = ChatRoom.objects.create(username = username,message = message,room = room , link = link)

        if img == "":
            obj.save()
        
        df = DateFormat(obj.date)
        f = df.format(get_format('DATETIME_FORMAT'))

        


        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username' : username,
                'msgtime' : f,
                'link' : link,
                'img' : img
                
            }
        )


    def chat_message(self, event):
        message = event['message']
        username = event['username']
        msgtime = event['msgtime']
        link = event['link']
        img = event['img']
       
        

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'username' : username,
            'msgtime' : msgtime,
            'link' : link,
            "img" : img
            
        }))
        
        


    def disconnect(self , *args,**kwargs):
        pass