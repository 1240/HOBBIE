from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = patterns('',
       # Examples:
       # url(r'^$', 'weekdays.views.home', name='home'),
       # url(r'^blog/', include('blog.urls')),

       url(r'^admin/', include(admin.site.urls)),
       url(r'^rooms/', include('room.urls')),
       url(r'^main/', include('mainpage.urls')),
       url(r'^auth/', include('loginsys.urls')),
       url(r'^account/', include('accounts.urls')),
       url(r'^', include('room.urls')),

)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()