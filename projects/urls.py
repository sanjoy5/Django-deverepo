from django.urls import path
from .views import *


urlpatterns = [
    path('',projects,name='projects'),
    path('project/<str:pk>/',project,name='single_project'),
    path('create-project/',createProject,name='create-project'),
    path('update-project/<str:pk>/',updateProject,name='update-project'),
    path('delete-project/<str:pk>/',deleteProject,name='delete-project'),
]
