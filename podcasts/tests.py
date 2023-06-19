from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse

from datetime import datetime

from .models import Episode

# Create your tests here.
class PodCastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title = "The Super Best Episode Ever",
            description = "What's cooler than a fridge? This episode of course!",
            pub_date = timezone.now(),
            link = "linkgoeshere",
            image = "image.linkgoeshere",
            podcast_name = "My Python Podcast",
            guid = "abc-123",
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.description, "What's cooler than a fridge? This episode of course!")
        self.assertEqual(self.episode.link, "linkgoeshere")
        self.assertEqual(self.episode.guid, "abc-123")
    
    def test_episode_str_representation(self):
        self.assertEqual(
            str(self.episode), "My Python Podcast: The Super Best Episode Ever"
        )
    
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "homepage.html")

    def test_homepage_list_contents(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, "The Super Best Episode Ever")