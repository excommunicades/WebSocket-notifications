from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notification(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title


class Subscription(models.Model):

    subscriber = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
    subscribed_to = models.ForeignKey(User, related_name='subscribers', on_delete=models.CASCADE)

    class Meta:

        unique_together = ('subscriber', 'subscribed_to')
