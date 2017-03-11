from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):

    def test_index_view_existence(self):
        """
        Index page should exist
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class AboutUsViewTests(TestCase):

    def test_about_us_view_existence(self):
        """
        About Us page should exist
        """
        response = self.client.get(reverse('about_us'))
        self.assertEqual(response.status_code, 200)
