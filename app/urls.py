from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:project_id>/', views.ProjectDetailView.as_view(), name='project-detail')
]