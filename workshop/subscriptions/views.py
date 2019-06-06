from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from workshop.subscriptions.forms import SubscriptionForm
from workshop.subscriptions.models import Subscriptions


def subscription(request):

    if request.method == 'POST':
        return create(request)

    else:
        return new(request)


def create(request):

    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request,
                      'subscriptions/subscription_form.html',
                      {'form': form})

    # Save Subscription
    #subscription = Subscriptions.objects.create(**form.cleaned_data)
    subscription = form.save()

    # send email
    _send_mail('subscriptions/subscription_email.txt',
               {'subscription':subscription},
               'Confirmação de Inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email)


    return HttpResponseRedirect('/subscription/{}/'.format(subscription.uuid))


def new(request):

    return render(request,
                  'subscriptions/subscription_form.html',
                  {'form':SubscriptionForm()})


def detail(request, uuid):

    subscription = Subscriptions.objects.get(uuid=uuid)

    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})


def _send_mail(template_name, context, subject,from_, to):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body,from_, [to, from_])