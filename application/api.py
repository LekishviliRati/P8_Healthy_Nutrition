import requests
import time


class Api:
    """Api Call to get products from OFF."""

    def __init__(self):
        self.products = []
        self.download_products()

    def download_products(self):
        """Comments."""
        API_REQUEST = "https://fr.openfoodfacts.org/cgi/search.pl?" \
                      "action=process&tagtype_0=countries&tag_contains_0=contains&" \
                      "tag_0=france&sort_by=unique_scans_n&page_size=750&json=true&" \
                      "fields=product_name_fr,code,brands,nutriscore_grade,url," \
                      "image_url,image_small_url,nutriments,categories"

        request = ""
        while request == "":
            time.sleep(2)
            try:
                request = requests.get(API_REQUEST)
                if request.status_code == 200:
                    self.products = request.json()["products"]

                else:
                    err = f"ERROR : {request.status_code}"
                    print(err)
                break
            except ValueError:
                time.sleep(3)
                continue

        products_with_no_empty_fields = []

        for article in self.products:
            if (
                article.get('product_name_fr')
                and article.get('brands')
                and article.get('url')
                and article.get('categories')
                and article.get('image_url')
                and article.get('image_small_url')
                and article.get('nutriments')
                and article.get('nutriscore_grade') is not None
            ):

                products_with_no_empty_fields.append(article)

        return products_with_no_empty_fields
