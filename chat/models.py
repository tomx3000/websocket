from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()

class Contacts(models.Model):
    user = models.ForeignKey(User, related_name="friends", on_delete=models.CASCADE)
    friends =models.ManyToMany("self",blank=True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    contact = models.ForeignKey(Contacts, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.user.username

class Chat(models.Model):
    participants = models.ManyToMany(Contacts,related_name="chats")
    messages = models.ManyToMany(Message,blank=True)


    def last_20_messages(self):

        return self.messages.objects.order_by("-created_at").all()[:20]
        
    
    def __str__(slef):
        return str(self.id)
