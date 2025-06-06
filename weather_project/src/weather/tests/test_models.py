from django.test import TestCase
from weather.models import City


class CityModelTest(TestCase):
    def test_city_creation(self):
        city = City.objects.create(name="Moscow")
        self.assertEqual(str(city.name), "Moscow")
