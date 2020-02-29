from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name="auithor_message", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_20_messages():
        return Message.objects.order_by("-created_at").all()[:20]
        
