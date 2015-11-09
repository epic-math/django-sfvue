"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
   url(r'^admin/', include(admin.site.urls)),
   url(r'^tinymce/', include('tinymce.urls')),
   url(r'^$', 'pages.views.MainHomePage'),  
   url(r'^cars/$', 'car.views.CarsAll'),
   url(r'^cars/(?P<carslug>.*)/$', 'car.views.SpecificCar'),
   url(r'^makes/(?P<makeslug>.*)/$', 'car.views.SpecificMake'),
   url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
   }),
   url(r'^register/$', 'driver.views.DriverRegistration'),
   url(r'^login/$', 'driver.views.LoginRequest'),
   url(r'^logout/$', 'driver.views.LogoutRequest'),
   url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done'),
   url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset', 
       {'post_reset_redirect' : 'django.contrib.auth.views.password_reset_done'},
        name="password_reset"),
   url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
   url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
   url(r'^profile/$', 'driver.views.Profile'),
   url('', include('social.apps.django_app.urls', namespace='social')),
   url(r'^custom_facebook_tab/sfvueCars$', 'custom_facebook_tab.views.SfvueCars'),
]
