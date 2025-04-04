from django.shortcuts import render
from portfolio.models import Project
# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {
        "projects":projects,
        "title":"Portfolio"
    }
    return render(request, "portfolio/index.html", context)

def detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project":project,
        "title":"Detail"
    }
    return render(request, "portfolio/detail.html", context)