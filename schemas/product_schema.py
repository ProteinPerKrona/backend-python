def product_serializer(product) -> dict:
    return {
        'name':str(product['name']),
        'ppk':float(product['ppk']),
        'weight':int(product['weight']),
        'price':int(product['price']),
        'protein':int(product['protein'])
    }
def products_serializer(products) -> list:
    return [product_serializer(product) for product in products]