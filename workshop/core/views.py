from django.shortcuts import render
from workshop.core.models import Speaker, Talk


def home(request):

    context = {
        'day_one': Talk.objects.filter(start__lt='12:00'),
        'day_two':Talk.objects.filter(start__gte='12:00')
    }
    return render(request, 'core/index.html', context)


def speaker(request):

    speakers = Speaker.objects.all()

    return render(request, 'core/speakers.html', {'speakers': speakers})


def about(request):
    return render(request, 'core/about.html')


def news(request):
    return render(request, 'core/news.html')


def events(request):
    return render(request, 'core/events.html')


def contact(request):
    return render(request, 'core/contact.html')