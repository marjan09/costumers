"""american URL Configuration

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
from django.conf.urls import url, include
from dbc.views import save_to_db,  delete,simple_upload,export,edit


urlpatterns = [
    path ('', save_to_db, name="form"),
    path ('display/', simple_upload),
    path('delete/<int:id>/', delete),
    path('edit/<int:id>/', edit),
    path('export/',export),
    path('admin/', admin.site.urls),
]
