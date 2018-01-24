from django.conf.urls import url
from django.contrib import admin
from apps.user_login import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/$', views.Users),
    url(r'^admin/', admin.site.urls),
]
