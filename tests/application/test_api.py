import unittest
from unittest.mock import patch
from application.api import Api

fake_response = {
    "count": 819400,
    "page": 1,
    "page_count": 750,
    "page_size": 750,
    "products": [
        {
            "brands": "Cristaline",
            "categories":
                "Beverages,Waters,Spring waters,Mineral waters,Natural mineral waters",
            "code": "3274080005003",
            "image_small_url":
                "https://images.openfoodfacts.org/images/products/327/408/000/5003/front_fr.626.200.jpg",
            "image_url":
                "https://images.openfoodfacts.org/images/products/327/408/000/5003/front_fr.626.400.jpg",
            "nutriments": {
                "alcohol": 0,
                "alcohol_100g": 0,
                "carbon-footprint-from-known-ingredients_product": 600,
                "chloride": 0.033,
                "chloride_100g": 0.033,
                "chloride_label": "Chlorure",
                "chloride_serving": 0.33,
                "chloride_unit": "mg",
                "chloride_value": 33,
                "energy": 0,
                "energy-kcal": 0,
                "energy-kcal_100g": 0,
                "energy-kcal_serving": 0,
                "energy-kcal_unit": "kcal",
                "energy-kcal_value": 0,
                "energy-kj": 0,
                "energy-kj_100g": 0,
                "energy_value": 0,
                "fat": 0,
                "fat_100g": 0,
                "fat_serving": 0,
                "fat_unit": "g",
                "fat_value": 0,
                "fiber": 0,
                "fiber_100g": 0,
                "fiber_serving": 0,
                "fiber_unit": "g",
                "fiber_value": 0,
                "fluoride": 0.001,
                "fluoride_100g": 0.001,
                "fluoride_label": "Fluorure",
                "fluoride_serving": 0.01,
                "fluoride_unit": "mg",
                "fluoride_value": 1,
                "magnesium": 0.026,
                "magnesium_100g": 0.026,
                "magnesium_label": "Magnésium",
                "magnesium_serving": 0.26,
                "magnesium_unit": "mg",
                "magnesium_value": 26,
                "nitrate": 0.002,
                "nitrate_100g": 0.002,
                "nitrate_label": "Nitrate",
                "nitrate_serving": 0.02,
                "nitrate_unit": "mg",
                "nitrate_value": 2,
                "nutrition-score-fr": 0,
                "nutrition-score-fr_100g": 0,
                "proteins": 0,
                "salt": 0,
                "salt_100g": 0,
                "silica_value": 26,
                "sodium": 0,
                "sodium_100g": 0,
                "sodium_serving": 0,
                "sodium_unit": "g",
                "sodium_value": 0,
                "sugars": 0,
                "sugars_100g": 0,
            },
        }]
}


class MockResponse:
    def __init__(self):
        self.status_code = 200

    def json(self):
        return fake_response


class TestApi(unittest.TestCase):

    @patch("requests.get", return_value=MockResponse())
    def test_download_products(self, second_positional_argument):
        obj = Api()
        # expected_products = fake_response[0]["products"]
        expected_products = fake_response.get("products")
        self.assertEqual(obj.products, expected_products)


if __name__ == '__main__':
    unittest.main()
