from rest_framework import serializers

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = [
            'pk',  # Исправлено добавлением запятой
            'owner',
            'title',
            'content',
        ]

    def create(self, validated_data):
        print('Creating notification...')
        user = self.context['request'].user  # Получение пользователя из контекста запроса
        print('Current user:', user)

        # Устанавливаем владельца уведомления
        validated_data['owner'] = user

        # Создаем и возвращаем уведомление
        return super().create(validated_data)