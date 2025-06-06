from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):
    def test_index_status_code(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_used(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "weather/index.html")
