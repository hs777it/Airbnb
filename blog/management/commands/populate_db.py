import random
from django.core.management.base import BaseCommand
from blog.models import Post,Category


class Command(BaseCommand):
    help = "Populates the database with random generated data."

    def handle(self, *args, **options):
        # populate the database with posts
        posts = [
            Post.objects.get_or_create(
                title="The O2 Arena", description="Peninsula Square, London SE10 0DX, United Kingdom"
            ),
            Post.objects.get_or_create(
                title="The Fillmore", description="1805 Geary Blvd, San Francisco, United States"
            ),
        ]


        # populate the database with categories
        # categories = ["Rock", "Pop", "Metal", "Hip Hop", "Jazz"]
        # for category in categories:
        #     ConcertCategory.objects.get_or_create(name=category)
        
        
        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))
