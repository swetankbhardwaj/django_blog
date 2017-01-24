from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', "polls.views.post_list"),
    url(r'^create/$', "polls.views.post_create"),
    url(r'^(?P<id>\d+)/$', "polls.views.post_detail" ,name="detail"),
    url(r'^update/$', "polls.views.post_update"),
    url(r'^delete/$', "polls.views.post_delete"),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]