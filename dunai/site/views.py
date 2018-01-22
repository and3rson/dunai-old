import os
import yaml

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

from .models import Feature, Project


def index(request):
    f = open(os.path.join(settings.BASE_DIR, 'dunai', 'files', 'cv.yaml'))
    with f:
        cv = yaml.load(f.read())
    return render(request, 'index.html', dict(
        cv=cv,
        features=Feature.objects.all(),
        projects=Project.objects.all()
    ))


def stars(request):
    return JsonResponse([
        dict(id=project.id, stars=project.get_stars())
        for project
        in Project.objects.all()
    ], safe=False)
