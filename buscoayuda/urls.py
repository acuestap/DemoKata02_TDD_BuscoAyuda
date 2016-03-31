from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'buscoayuda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('polls.urls', namespace="principal")),
    url(r'^admin/', include(admin.site.urls)),
]
