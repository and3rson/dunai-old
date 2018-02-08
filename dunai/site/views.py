import os
from time import time
from threading import Lock

import yaml
import requests
from django.urls import reverse
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, HttpResponse

from .models import Feature, Project


def get_cv():
    cvfile = open(os.path.join(settings.BASE_DIR, 'dunai', 'files', 'cv.yaml'))
    with cvfile:
        return yaml.load(cvfile.read())


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


GEN_LAST = 0
GEN_LOCK = Lock()


def print_pdf(request):
    global GEN_LAST
    GEN_LOCK.acquire()
    try:
        if GEN_LAST + 3600 < time():
            response = requests.get(request.build_absolute_uri('/print'))
            with open('/tmp/print.html', 'wb') as html:
                html.write(response.content)
            response = requests.post(
                'http://wkhtmltopdf',
                files=dict(
                    file=(
                        'print.html',
                        open('/tmp/print.html', 'rb')
                    )
                )
            )
            with open('/tmp/print.pdf', 'wb') as pdf:
                pdf.write(response.content)
            GEN_LAST = time()
    finally:
        GEN_LOCK.release()
    with open('/tmp/print.pdf', 'rb') as pdf:
        return HttpResponse(pdf.read(), content_type='application/pdf')
