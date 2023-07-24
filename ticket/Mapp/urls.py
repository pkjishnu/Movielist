"""
URL configuration for ticket project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from Mapp import views
app_name='Mapp'
urlpatterns = [
    path('', views.home.as_view(),name="home"),
# path('addmovi', views.addmovie,name="add5"),
# path('add', views.add1,name="add1"),
path('add', views.add1.as_view(),name="add1"),
# path('update/<int:p>', views.update,name="update"),
path('update/<int:pk>', views.update.as_view(),name="update"),
#path('delete/<int:p>', views.delete,name="delete"),
path('delete/<int:pk>', views.delete.as_view(),name="delete"),
# path('view/<int:p>', views.view,name="view"),
path('view/<int:pk>', views.view.as_view(),name="view"),
]
