from django.conf.urls import include, url
from django.contrib import admin
from main import views as mainViews

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	 url(r'^$', mainViews.home),
    url(r'^login/', mainViews.login, name='login'),
    url(r'^register/', mainViews.register, name='register'),
]
