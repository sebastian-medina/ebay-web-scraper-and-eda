from .constants import BRANDS

def product_brand(product_name):
    for k,v in BRANDS.items():
        if k in product_name:
            return v
