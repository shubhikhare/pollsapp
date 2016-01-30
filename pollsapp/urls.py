from django.conf.urls import include, url
from django.contrib import admin
from  polls import views


urlpatterns = [
    # Examples:
    url(r'^$', views.index),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
