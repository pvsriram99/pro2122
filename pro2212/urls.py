"""pro2212 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from a2zapp import views
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base),
    path('home/', views.home),
    path('hrmanager/', views.hrman),
    path('accounts/', include('django.contrib.auth.urls')),
    path('employee/', views.emp),
    path('empform/', views.empfrm),
    path('empdata/', views.empdata),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
    path('addnews/', views.newsfrm),
    path('latestnews/', views.latestnews),
    path('addholiday/', views.calfrm),
    path('holcal/', views.holcal),
    path('csv/', views.getfile)

]
