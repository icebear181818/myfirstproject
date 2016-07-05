from django.conf.urls import url
import views
urlpatterns=[
    #/music/
    url(r'^$',views.index,name='index'),
    #/music/711/
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
]