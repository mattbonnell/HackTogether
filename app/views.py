from django.shortcuts import render
from django.views.generic import *
from .models import *
# Create your views here.


def index(request):

    context = {'user': request.user}

    if request.user.is_authenticated:
        context["login_button_text"] = "Hello, " + request.user.first_name
    else:
        context["login_button_text"] = "Login"
    return render(request, 'app/index.html', context)


class ProjectDetailView(DetailView):

    model = Project

    template_name = 'app/project-detail.html'

    context_object_name = "project"

   # num_of_developers_needed = object.specialities_needed.filter(is_developer_speciality=True).count()
   # num_of_designers_needed = object.specialities_needed.filter(is_designer_speciality=False).count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       # context['num_of_developers_needed'] = self.num_of_developers_needed
       # context['num_of_designers_needed'] = self.num_of_designers_needed
        return context


def project_list_view(request):

    user_profile = UserProfile.objects.get(user_id=request.user.id)

    if user_profile.is_developer:
        project_list = list(Project.objects.filter(developer_needed=True))
    else:
        project_list = list(Project.objects.filter(designer_needed=True))

    context = {'project_list': project_list}

    return render(request, 'app/project-list.html', context)


def profile_detail_view(request, profile_id):

    user_profile = UserProfile.objects.get(user_id=request.user.id)

    context = {'user_profile': user_profile}

    return render(request, 'app/profile-detail.html', context)
