from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/', views.project_list_view, name='project-list'),
    path('project/<int:project_id>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('profile/<int:profile_id>/', views.profile_detail_view, name='profile-detail')
]
