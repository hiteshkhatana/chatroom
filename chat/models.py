from django.db import models

import datetime

# Create your models here.
class ChatRoom(models.Model):
    room = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    message = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.username} - {self.room}'
