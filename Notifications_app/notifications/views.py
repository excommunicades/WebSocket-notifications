from typing import Any
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.models import User
from notifications.models import Notification, Subscription 


class NotificationView(TemplateView):

    template_name = 'notifications/notification.html'

    def post(self, request, *args, **kwargs):

        type = request.POST.get('type')

        match type:

            case 'crud':

                operation = request.POST.get('operation_type')

                pk = request.POST.get('pk')
                print(pk)
                title = request.POST.get('title')

                content = request.POST.get('content')

                match operation:

                    case 'create':

                        Notification.objects.create(owner=request.user, title=title, content=content)

                        print('created')

                    case 'update':

                        notification = Notification.objects.get(pk=pk)

                        if title:

                            notification.title = title

                        if content:

                            notification.content = content

                        notification.save()

                        print('updated')

                    case 'delete':

                        notification = Notification.objects.get(pk=pk)

                        notification.delete()

                        print('deleted')

                return HttpResponse('Operation successfully executed!')

            case 'subscribe':

                subscribe_to_user = request.POST.get('user_to_subscribe')
                user = User.objects.get(pk=int(subscribe_to_user))
                if subscribe_to_user:

                    Subscription.objects.create(subscriber=request.user, subscribed_to=user)

                    return HttpResponse('Successfully subscribed.')

                else:

                    return HttpResponse('User doest not exist.')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        notifications = Notification.objects.all()

        users = User.objects.all()

        context = super().get_context_data(**kwargs)

        subscribers = Subscription.objects.filter(subscriber=users)

        context['notifications'] = notifications
        context['users'] = users
        context['subscribers'] = subscribers
        return context

# TODO: subscribers, websockets, notifies