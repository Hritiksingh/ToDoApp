from django.conf.urls import include, url
from . import views

app_name = "Todo"

urlpatterns = [
    # it will take us upto the index page of the website.
    url(r'^$', views.IndexView.as_view(), name="index"),

    # this will open a form to create new tasks
    url(r'dailyworks-add/$', views.DailyWorksCreate.as_view(), name='dailyworks_add'),

    # /Todo/dailyworks/2/delete/
url(r'^(?P<work_id>[0-9]+)/delete_dailyworks/$', views.delete_dailyworks, name='delete_dailyworks'),

    #url(r'^(P<pk>[0-9]+)/$')
    # this url will redirect us to index page after deleting the selected Task
   # url(r'dailyworks/delete/(?P<pk>[0-9]+)/delete/$', views.DailyWorksDelete.as_view(), name='dailyworks_delete'),
    #url(r'^dailyworks_delete', views.remove, name="dailyworks_delete"),
]