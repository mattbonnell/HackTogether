from django.shortcuts import render
from django.views.generic import *
from .models import *
# Create your views here.


def index(request):
    context = {'user': request.user}
    return render(request, 'app/index.html', context)


class ProjectDetailView(DetailView):

    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def project_list_view(request):

    user_profile = UserProfile.objects.get(user__id=request.user.id)

    if user_profile.is_developer:
        project_list = list(Project.objects.filter(developer_needed=True))
    else:
        project_list = list(Project.objects.filter(designer_needed=True))

    context = {'project_list': project_list}

    return render(request, 'app/project-list.html', context)


class ProfileDetailView(DetailView):

    model = UserProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
