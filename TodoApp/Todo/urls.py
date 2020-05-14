from django.conf.urls import include, url
from . import views

app_name = "Todo"

urlpatterns = [
    # it will take us upto the index page of the website.
    url(r'^$', views.IndexView.as_view(), name="index"),

    # this will open a form to create new tasks
    url(r'dailyworks/add/$', views.DailyWorksCreate.as_view(), name='dailyworks_add'),
]