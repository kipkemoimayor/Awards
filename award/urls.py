from . import views
from django.conf.urls import url

#url urlpatterns

urlpatterns=[
    url(r'^$',views.index, name='index'),

]
