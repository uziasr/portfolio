from django.shortcuts import render, get_object_or_404
from . models import Project

# Create your views here.
def uzias(request):
    projects = Project.objects
    return render(request, 'projects/home.html', {'projects': projects})

def detail(request, project_id):
    project_detail = get_object_or_404(Project, pk=project_id)
    #if (project_detail):
    return render(request, 'projects/detail.html', {'project': project_detail})
