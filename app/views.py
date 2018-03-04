from django.shortcuts import render
from django.views.generic import DetailView
from .models import Project
# Create your views here.


def index(request):
    context = {'user': request.user}
    return render(request, 'app/index.html', context)


class ProjectDetailView(DetailView):

    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context