from . import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token


#url urlpatterns

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url(r'project/post/$',views.post,name='post'),
    url(r'^user/profile/$',views.profile,name='profile'),
    url(r'^project/(\d+)/',views.project_detail,name='details'),
    url(r'^search/projects/results/$',views.search,name="search"),
    # url(r'^ajax/review/(\d+)$',views.ajaxRequest,name='review'),
    url(r'^api/projects/$',views.ProjectList.as_view()),
    url(r'^api/profile/$',views.ProfileList.as_view()),
    url(r'^token/', obtain_auth_token),
    url(r'^developer/api/$',views.apiView,name='api'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
