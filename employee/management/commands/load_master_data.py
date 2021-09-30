import datetime
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    def handle(self, *args, **options):
        groups = ['admin', 'employee']
        for group in groups:
            g, _ = Group.objects.get_or_create(name=group)
        print("Groups Loaded")
