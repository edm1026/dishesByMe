"""dishesByMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/dishesByMe/')),
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', include('home.urls')),
]

"""
urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/home/')),  #might need to try the above urlpatterns; 'mysite.view.home', name='home'
                       #url(r'^home/', include('home.urls')),
    url(r'^admin/', include('admin.site.urls')),
)
"""


#if settings.DEBUG:
#    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
from django.conf.urls import patterns, include url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'mysite.view.home', name='home'),
    url(r'^home/', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
"""
