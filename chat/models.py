from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Thread(models.Model):
    participants = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Thread {self.id}'

    def last_message(self):
        return self.messages.order_by('-created').first()


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    thread = models.ForeignKey(Thread, related_name='messages', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message {self.id}'

    class Meta:
        ordering = ('created',)
