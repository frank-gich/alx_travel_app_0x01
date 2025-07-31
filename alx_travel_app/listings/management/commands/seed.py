from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing
from faker import Faker
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("Deleting old data..."))
        Listing.objects.all().delete()

        self.stdout.write(self.style.NOTICE("Creating users..."))
        for i in range(3):
            User.objects.get_or_create(username=f'user{i}', defaults={'email': fake.email(), 'password': 'testpass'})

        users = User.objects.all()

        self.stdout.write(self.style.SUCCESS("Creating listings..."))
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(),
                description=fake.paragraph(),
                location=fake.city(),
                price_per_night=random.uniform(50, 300),
                host=random.choice(users)
            )

        self.stdout.write(self.style.SUCCESS("Seeding completed successfully."))
