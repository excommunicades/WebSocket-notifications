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

                return HttpResponse('Operation successfully executed! Back to notifications -> <a href="nf">notifications</a> ')

            case 'subscribe':

                subscribe_to_user = request.POST.get('user_to_subscribe, back to notifications -> <a href="nf">notifications</a> ')
                user = User.objects.get(pk=int(subscribe_to_user))
                if subscribe_to_user:

                    if user == request.user:

                        return HttpResponse('You cant subscribe on yourself, back to notifications -> <a href="nf">notifications</a> ')

                    try:
                        print(request.user)
                        subs = Subscription.objects.get(subscriber=request.user, subscribed_to=user)

                        if subs:

                            subs.delete()

                            return HttpResponse('Successfully unsubscribed, back to notifications -> <a href="nf">notifications</a> ')

                    except Subscription.DoesNotExist:

                        Subscription.objects.create(subscriber=request.user, subscribed_to=user)

                        return HttpResponse('Successfully subscribed, back to notifications -> <a href="nf">notifications</a> ')

                else:

                    return HttpResponse('User doest not exist, back to notifications -> <a href="nf">notifications</a> ')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        """return context data for django template language"""

        notifications = Notification.objects.all()

        users = User.objects.all()

        context = super().get_context_data(**kwargs)

        subscribers = Subscription.objects.all()

        context['notifications'] = notifications
        context['users'] = users
        context['subscribers'] = subscribers
        return context

# TODO: subscribers, websockets, notifies 