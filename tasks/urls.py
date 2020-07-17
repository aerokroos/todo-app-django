from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, PageView
from django.urls import path

urlpatterns = [
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('new/', TaskCreateView.as_view(), name='task_new'),
    path('home/', TaskListView.as_view(), name='home'),
    path('', PageView.as_view(), name='base'),
    


    
]