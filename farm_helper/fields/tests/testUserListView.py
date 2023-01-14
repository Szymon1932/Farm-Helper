from django.test import TestCase
from models import *
from django.urls import reverse

class PlantListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_fields = 10
        for plant_id in range(number_of_fields):
            price=plant_id*30 + 800
            Plant.objects.create(plant_name=f"Plant{plant_id}", seed_price=f"{price}")
    
    def test_url_exists(self):
        response = self.client.get("/plants")
        self.assertEqual(response.status_code, 200)
    
    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("show-plants"))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('show-plants'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fields/show/plant.html')