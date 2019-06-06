from django.contrib import admin
from django.urls import path
from workshop.core.views import home, speaker, \
    about, news, events, contact


from workshop.subscriptions.views import subscription, detail

urlpatterns = [

    path('', home, name='home'),
    path('speakers/', speaker, name='speaker'),
    path('about/', about, name='about'),
    path('news/', news, name='news'),
    path('events/', events, name='events'),
    path('contact/', contact, name='contact'),
    path('subscription/', subscription, name='subscription'),
    path('subscription/<str:uuid>/', detail),

    path('admin/', admin.site.urls),
]
