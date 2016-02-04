from django.conf.urls import include, url
from django.contrib import admin
from main import views as mainViews

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	 url(r'^$', mainViews.home, name='home'),
    url(r'^accounts/login/', mainViews.login, name='login'),
    url(r'^accounts/logout/', mainViews.logout, name='logout'),
    url(r'^accounts/register/', mainViews.register, name='register'),
    url(r'^profile/([0-9]+)/$', mainViews.profile, name='profile'),
]
