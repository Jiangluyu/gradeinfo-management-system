"""dbclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from login import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('userinfo/', views.user_info),
    path('classinfo/', views.class_info),
    path('forget/', views.forget),
    path('forget/retrieve/', views.retrieve),
    path('forget/resetpwd/', views.resetpwd),
    path('delete/', views.grade_delete),
    path('update/', views.grade_update, name='gradeupdate'),
    url(r'^classinfo/gradeadd/$', views.grade_add, name='gradeadd'),
    url(r'^classinfo/(\d+)/$', views.grade_info, name='gradeinfo'),
    url(r'^captcha', include('captcha.urls')),
]
