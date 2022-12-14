from django.urls import path
from . import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
path('taskentry/', views.form),
path('previoustask/', views.previoustask),
path('futuretask/', views.futuretask),
path('tasks/', views.alltasks),
path('update/', views.update),
path('between/', views.between),
path('delete/', views.delete),
path('form/', views.form),
]
