from django.urls import path
from .views import (apiurlsoverview,
                    tasklist,
                    taskdetail,
                    createtaskview,
                    updatetaskview,
                    deletetaskview,)
from django.views.generic import TemplateView

urlpatterns = [
    path('api/', apiurlsoverview,name='apiurllist'),
    path('Task-list/', tasklist,name='tasklist'),
    path('Task-detail/<str:pk>/', taskdetail,name='taskdetail'),
    path('Task-create/', createtaskview,name='createtask'),
    path('Task-update/<str:pk>/', updatetaskview,name='updatetask'),
    path('Task-delete/<str:pk>/', deletetaskview,name='deletetask'),
    path('', TemplateView.as_view(template_name='index.html'))
]