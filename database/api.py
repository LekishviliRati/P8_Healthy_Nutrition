import requests
import json


class Api:
    """Api Call to get products from OFF."""

    def __init__(self):
        # self.products = []
        self.download_products()

    def download_products(self):
        """Comments."""
        API_REQUEST = "https://fr.openfoodfacts.org/cgi/search.pl?" \
                      "action=process&tagtype_0=countries&tag_contains_0=contains&" \
                      "tag_0=france&sort_by=unique_scans_n&page_size=750&json=true&" \
                      "fields=product_name_fr,code,brands,nutriscore_grade,url," \
                      "image_url,image_small_url,nutriments,categories"

        api_call = requests.get(API_REQUEST)
        api_call_text = api_call.text
        json_data = json.loads(api_call_text)
        product_list = json_data["products"]

        products_with_no_empty_fields = []
        for p in product_list:
            if (
                    p.get('product_name_fr')
                    and p.get('brands')
                    and p.get('url')
                    and p.get('categories')
                    and p.get('image_url')
                    and p.get('image_small_url')
                    and p.get('nutriments')
                    and p.get('nutriscore_grade') is not None
            ):
                products_with_no_empty_fields.append(p)

        return products_with_no_empty_fields
