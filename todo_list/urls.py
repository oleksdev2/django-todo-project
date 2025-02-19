from django.urls import path
from django.views.generic import TemplateView

# вместо from .views import index_view, где указывается index_view
from . import views  # в url уже надо указывать views.index_view, но не надо импортировать каждую вьюху

app_name = 'todo_list'

urlpatterns = [
    #path('', TemplateView.as_view(template_name='todo_list/index.html'), name='index'),  # работает без вьюхи
    #path('', views.index_view, name='index'),
    #path('', views.ToDoListIndexView.as_view(), name='index'),
    path('', views.ToDoListIndexView.as_view(), name='index'),
    path('list/', views.ToDoListView.as_view(), name='list'),
]
