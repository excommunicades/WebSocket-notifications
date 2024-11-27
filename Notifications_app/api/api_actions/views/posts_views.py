from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from notifications.models import Notification
from api.api_actions.serializers.posts_serializers import NotificationSerializer

# from api.signals import post_created_signal


class NotificationViewSet(viewsets.ModelViewSet):

    queryset = Notification.objects.all()

    serializer_class = NotificationSerializer

