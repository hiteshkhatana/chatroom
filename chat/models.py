from django.db import models

from django.utils import timezone

# Create your models here.
class ChatRoom(models.Model):
    room = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    message = models.CharField(max_length=100 , blank=True)
    img = models.ImageField(upload_to = 'attachments' , blank = True)
    link = models.CharField(max_length=100 , blank=True)
    date = models.DateTimeField(auto_now_add= timezone.now())

    def __str__(self):
        return f'{self.username} - {self.room}'


class Privatenotifications(models.Model):
    sender = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} to {self.receiver} - {self.seen}'