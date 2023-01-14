from django.test import TestCase
from .models import *
from django.urls import reverse

class PlantListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_plants = 10
        for plant_id in range(number_of_plants):
            price=plant_id*30 + 800
            Plant.objects.create(plant_name=f"Plant{plant_id}", seed_price=f"{price}")
    
    def test_url_exists(self):
        response = self.client.get("/plants/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("show-plants"))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('show-plants'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fields/show/plant.html')


class PlantModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Plant.objects.create(plant_name="Jęczmień", seed_price=820)
    def test_string_method(self):
        plant = Plant.objects.get(id=1)
        expected_string =plant.plant_name
        self.assertEqual(str(plant), expected_string)

class FertilizerListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_fertilizers = 10
        for fertilizer_id in range(number_of_fertilizers):
            price=fertilizer_id*30 + 800
            Fertilizer.objects.create(fertilizer_name =f"Fertilizer{fertilizer_id}", price=f"{price}")
    
    def test_url_exists(self):
        response = self.client.get("/fertilizers/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("show-fertilizers"))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('show-fertilizers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fields/show/fertilizer.html')

class FertilizerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Fertilizer.objects.create(fertilizer_name="Nawoz1", price=820)
    def test_string_method(self):
        fertilizer = Fertilizer.objects.get(id=1)
        expected_string =fertilizer.fertilizer_name
        self.assertEqual(str(fertilizer), expected_string)

class PlantPriceListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_plant_price = 10
        plant=Plant.objects.create(plant_name="Jęczmień", seed_price=800,)
        for plant_price_id in range(number_of_plant_price):
            price=plant_price_id*30 + 800
            PlantPrice.objects.create(plant = plant, price=f"{price}", date="2020-01-01", is_predicted=0)
    
    def test_url_exists(self):
        response = self.client.get("/plant_prices/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("show-plant_prices"))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('show-plant_prices'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fields/show/plantPrice.html') 

class PlantPriceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        plant=Plant.objects.create(plant_name="Jęczmień", seed_price=800)
        PlantPrice.objects.create(plant=plant, price=820, date="2020-01-01", is_predicted=0)
    def test_string_method(self):
        plant_price  = PlantPrice.objects.get(id=1)
        expected_string = str(plant_price.price)
        self.assertEqual(str(plant_price), expected_string)

class PredictedCropListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_predicted_crops = 10

        plant=Plant.objects.create(plant_name="Jęczmień", seed_price=800)
        class_field=ClassField.objects.create()

        for predicted_crop_id in range(number_of_predicted_crops):
            crop_mass=predicted_crop_id*0.4 + 7
            PredictedCrop.objects.create(predicted_crop_name = f"Pred.name{predicted_crop_id}",plant = plant, crop_mass=f"{crop_mass}", class_field=class_field)
    
    def test_url_exists(self):
        response = self.client.get("/predicted_crops/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("show-predicted_crops"))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('show-predicted_crops'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fields/show/predictedCrop.html') 

class PredictedCropModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        plant=Plant.objects.create(plant_name="Jęczmień", seed_price=800)
        class_field=ClassField.objects.create()
        PredictedCrop.objects.create(predicted_crop_name = "Pred.name1",plant = plant, crop_mass=10, class_field=class_field)

    def test_string_method(self):
        predicted_crop= PredictedCrop.objects.get(id=1)
        expected_string = str(predicted_crop.predicted_crop_name)
        self.assertEqual(str(predicted_crop), expected_string)



    predicted_crop = models.ForeignKey(
        'PredictedCrop', on_delete=models.CASCADE)
    fertilizer = models.ForeignKey('Fertilizer', on_delete=models.CASCADE)
    fertilizer_mass = models.DecimalField(max_digits=10, decimal_places=2)


class FertilizationPlanListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_fertilization_plan = 10
        plant=Plant.objects.create(plant_name="Jęczmień", seed_price=800)
        class_field=ClassField.objects.create()
        predicted_crop = PredictedCrop.objects.create(predicted_crop_name = "Pred.name1",plant = plant, crop_mass=10, class_field=class_field)
        fertilizer = Fertilizer.objects.create(fertilizer_name="Nawoz1", price=820)

        for fertilization_plan_id in range(number_of_fertilization_plan):
            fertilizer_mass=fertilization_plan_id*0.1
            FertilizationPlan.objects.create(predicted_crop = predicted_crop, fertilizer=fertilizer, fertilizer_mass=f"{fertilizer_mass}")
    
    def test_url_exists(self):
        response = self.client.get("/fertilization_plans/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("show-fertilization_plans"))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('show-fertilization_plans'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fields/show/fertilizationPlan.html') 

class FertilizationPlanModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        plant=Plant.objects.create(plant_name="Jęczmień", seed_price=800)
        class_field=ClassField.objects.create()
        predicted_crop = PredictedCrop.objects.create(predicted_crop_name = "Pred.name1",plant = plant, crop_mass=10, class_field=class_field)
        fertilizer = Fertilizer.objects.create(fertilizer_name="Nawoz1", price=820)
        FertilizationPlan.objects.create(predicted_crop = predicted_crop, fertilizer=fertilizer, fertilizer_mass=0.4)
    
    def test_string_method(self):
        fertilization_plan = FertilizationPlan.objects.get(id=1)
        expected_string = str(fertilization_plan.fertilizer_mass)
        self.assertEqual(str(fertilization_plan), expected_string)


class FieldListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_fields = 10
        user=User.objects.create()
        classfield=ClassField.objects.create()
        for field_id in range(number_of_fields):
            area =field_id*1.5
            Field.objects.create(field_name = f"Field{field_id}", area=f"{area}", user = user, class_field = classfield)
    
    def test_url_exists(self):
        response = self.client.get("/fields/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("show-fields"))
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('show-fields'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fields/show/field.html')

class FieldModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user=User.objects.create()
        classfield=ClassField.objects.create()
        Field.objects.create(field_name="Field1", area=4.2, user = user, class_field = classfield)
    def test_string_method(self):
        field  = Field.objects.get(id=1)
        expected_string = str(field.field_name)
        self.assertEqual(str(field), expected_string)


# Create your tests here.
#brak przyszłych cen powoduje błąd predykcji -> fix