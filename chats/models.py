from django.db import models

class Message(models.Model):
    """Модель сообщения"""

    id = models.AutoField(primary_key=True, unique=True)
    text = models.CharField(max_length=255)
