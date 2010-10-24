from django.conf.urls.defaults import *
from muril.views import * 

urlpatterns = patterns('',
    (r'^$', index),
    (r'^(?P<link_id>\d+)/$', expand_link),
)
