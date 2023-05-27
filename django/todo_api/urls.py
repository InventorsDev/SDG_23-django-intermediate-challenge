from django.urls import path
from . import views

urlpatterns = [
    path('',views.TaskList.as_view(),name='task_list'),
    path('<task_id>/',views.TaskDetail.as_view(),name='task_detail'),
    path('<task_id>/completed/',views.TaskComplete.as_view(),name='task_complete'),
]
