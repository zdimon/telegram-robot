from django.db import models

# Create your models here.

class Room(models.Model):
    id_key =  models.CharField(max_length=250)
    name =  models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class RoomMessage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    sender_id = models.CharField(max_length=50)