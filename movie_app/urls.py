"""
URL configuration for movie_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views  # Import the view from the current app


urlpatterns = [
    path('home/', views.home, name='home'), # Route for the home view
    path('create/',views.create, name='create'),  # Route for the create view
    path('edit/<pk>',views.edit, name='edit'),  # Route for the edit view
    path('delete/<pk>',views.delete, name='delete'),  # Route for the delete view
    path('list/',views.list, name='list'),
    path('edit_all/', views.edit_all, name='edit_all'),  # Route for the edit all view
    path('delete_all/', views.delete_all, name='delete_all'),
    path('search/', views.search, name='search'),
]
