"""hellosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from helloapp.views import HelloWorldView, HelloNameView, GoodbyeDjangoView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', HelloWorldView.as_view(), name='hello_world'),
    path('hello/<name>', HelloNameView.as_view(), name='hello_name'),
    path('hello/goodbye/<name>', GoodbyeDjangoView.as_view(), name='goodbye_django'),
]

urlpatterns += staticfiles_urlpatterns()