from django.urls import path

from notifications.views import NotificationView

urlpatterns = [
    path('nf', NotificationView.as_view(), name='notifications-view')
]
