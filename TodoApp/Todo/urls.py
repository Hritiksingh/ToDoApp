from django.conf.urls import include, url
from . import views

app_name = "Todo"

urlpatterns = [
    # it will take us upto the index page of the website.
    url(r'^$', views.IndexView.as_view(), name="index"),

    # this will open a form to create new tasks
    url(r'dailyworks-add/$', views.DailyWorksCreate.as_view(), name='dailyworks_add'),

    # /Todo/dailyworks/2/delete/
    url(r'^(?P<work_id>[0-9]+)/delete-dailyworks/$', views.delete_dailyworks, name='delete_dailyworks'),

    # url to delete all the Tasks at once
    url(r'^dailyworks-deleteAll/$', views.DeleteAllDailyWorks, name='dailyworks_deleteAll'),

]