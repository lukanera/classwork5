from . import views
from django.urls import path

urlpatterns = [
    path('tasks/', views.TaskListCreateView.as_view()),
    path('tasks/<int:pk>', views.TaskRetriveUpdateDeleteView.as_view())
]
