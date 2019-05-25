from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

#url urlpatterns

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'project/post/$',views.post,name='post'),
    url(r'^user/profile/$',views.profile,name='profile'),
    url(r'^project/(\d+)/',views.project_detail,name='details'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
