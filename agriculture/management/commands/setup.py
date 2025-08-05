from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser with the provided environment variables'

    def handle(self, *args, **options):
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')

        if not all([username, password]):
            self.stdout.write(self.style.ERROR('Skipping superuser creation: DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD not set.'))
            return

        if not User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS(f'Creating superuser: {username}'))
            User.objects.create_superuser(username=username, password=password, email=email)
        else:
            self.stdout.write(self.style.WARNING(f'Superuser {username} already exists. Skipping.'))