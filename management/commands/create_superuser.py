from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError, ProgrammingError

class Command(BaseCommand):
    help = "Create a super use automatically"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = "Tobi"
        email = "tobi@gmail.com"
        password = "@jimmy1776"


        try:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created succesfully!"))
            else:
                self.stdout.write(self.style.WARNING(f"Superuser '{username}' already exists."))
        except (OperationalError, ProgrammingError) as e:
            self.stderr.write(self.style.ERROR(f"Database not ready: {e}"))