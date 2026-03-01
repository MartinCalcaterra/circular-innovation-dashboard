"""
URL configuration for cic_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("initial/", views.initial_dashboard, name="initial_dashboard"),
    path("senior/", views.senior_dashboard, name="senior_dashboard"),
    path("leader/", views.leader_dashboard, name="leader_dashboard"),
    path("admin/", views.admin_dashboard, name="admin_dashboard"),
]
