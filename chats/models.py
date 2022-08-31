from django.db import models
#from django.contrib.auth.models import User


class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    text = models.CharField(max_length=255)
