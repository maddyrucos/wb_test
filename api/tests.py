from rest_framework.test import APITestCase
from django.urls import reverse
from wb_parser.models import Product

class ProductAPITestCase(APITestCase):
    def setUp(self):
        Product.objects.create(
            nm_id=1001, name="Phone A", price_basic=10000, price_basic_rub=12000,
            price_total=9000, price_total_rub=11000, rating=4.5, feedbacks=100
        )
        Product.objects.create(
            nm_id=1002, name="Phone B", price_basic=5000, price_basic_rub=6000,
            price_total=4500, price_total_rub=5500, rating=3.8, feedbacks=50
        )
        Product.objects.create(
            nm_id=1003, name="Laptop C", price_basic=20000, price_basic_rub=24000,
            price_total=18000, price_total_rub=22000, rating=4.9, feedbacks=200
        )

    def test_get_all_products(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)

    def test_filter_by_min_price_total(self):
        response = self.client.get("/api/products/?price_total_min=8000")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_max_price_total(self):
        response = self.client.get("/api/products/?price_total_max=5000")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["nm_id"], 1002)

    def test_filter_by_rating_min(self):
        response = self.client.get("/api/products/?rating_min=4")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_filter_by_name_icontains(self):
        response = self.client.get("/api/products/?name=phone")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_combined_filters(self):
        response = self.client.get("/api/products/?price_total_min=8000&rating_min=4.5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        ids = [product["nm_id"] for product in response.data]
        self.assertIn(1001, ids)
        self.assertIn(1003, ids)
