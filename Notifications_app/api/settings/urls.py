from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.api_actions.views.posts_views import NotificationViewSet

router = DefaultRouter()
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]