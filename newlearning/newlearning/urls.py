from django.conf.urls import url, include
from django.contrib import admin
# from . import views

urlpatterns = [
    #/admin/
    url(r'^admin/', admin.site.urls),

    #/music/
    url(r'^music/', include('music.urls')),
    #
    # #/music/album_id
    # url(r'^(?P<album_id>[0-9]+)$', views.details, name='details')
]