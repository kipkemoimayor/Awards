from . import views
from django.conf.urls import url

#url urlpatterns

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'project/post/$',views.post,name='post'),
]
