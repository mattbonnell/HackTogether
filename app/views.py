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


class ProjectListView(ListView):

    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProfileDetailView(DetailView):

    model = UserProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


