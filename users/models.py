from django.db import models

# Create your models here.
class ProfileModel(models.Model):
    username = models.CharField(max_length=20)
    dp = models.ImageField(upload_to = "images" , default = 'images/dp.jpg ')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.username