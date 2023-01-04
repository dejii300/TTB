from operator import index
from django.urls import path
from . import views


urlpatterns = [
    path('', views.firsttemplate, name='Home'),
    path('Projects/', views.myfirst, name='Project'), 
    path('Projects/Project/<str:pk>/', views.Project, name='project'),
    path('Projects/Add project/', views.createproject, name='createproject'),
    path('Projects/Project/update/<str:pk>/', views.updateproject, name='update-project'),
    path('Projects/Project/Delete/<str:pk>/', views.deleteproject, name='delete'),
]