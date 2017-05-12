"""RemindMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'reminders'
urlpatterns = [
    url(r'^$',views.upcoming_view, name = 'upcoming'),
    url(r'^all/$',views.all_view, name = 'all'),
    url(r'^add/$',views.add_reminder_view, name = 'add'),
    url(r'^remove/(?P<rem_id>.*)/$',views.remove_view, name = 'remove'),
    url(r'^update/(?P<rem_id>.*)/$',views.update_reminder_view, name = 'update'),
    url(r'^(?P<rem_id>.*)/$',views.detail_view, name = 'detail'),
]
