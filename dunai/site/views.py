import os
import yaml

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse

from .models import Feature, Project


def get_cv():
    f = open(os.path.join(settings.BASE_DIR, 'dunai', 'files', 'cv.yaml'))
    with f:
        return yaml.load(f.read())


def index(request):
    return render(request, 'index.html', dict(
        cv=get_cv(),
        features=Feature.objects.all(),
        projects=Project.objects.all()
    ))


def print(request):
    return render(request, 'print.html', dict(
        cv=get_cv(),
        projects=Project.objects.all()
    ))


def print_pdf(request):
    pass
    # response = HttpResponse(get_pdf(), content_type='application/pdf')
    # return response


# def stars(request):
#     return JsonResponse([
#         dict(id=project.id, stars=project.get_stars())
#         for project
#         in Project.objects.all()
    # ], safe=False)
