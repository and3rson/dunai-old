from time import sleep

from django.core.management import BaseCommand

from dunai.site.models import Project


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        while True:
            for project in Project.objects.all():
                project.update_stars()
                project.save()
            sleep(3600)
