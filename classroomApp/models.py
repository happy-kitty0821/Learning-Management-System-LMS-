from django.db import models

# Create your models here.
class ClassRooms(models.Model):
    roomCode = models.CharField(max_length=10, unique=True, primary_key=True, null=False)
    roomName = models.CharField(max_length=100, unique=True, null=False, default="")
    createdOn = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.roomName:
            self.roomName = self.roomCode
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.roomName} ({self.roomCode})"
