def product_serializer(product) -> dict:
    return {
        'name':str(product['name']),
        'ppk':str(product['ppk'])
    }
def product_serializer(products) -> list:
    return [product_serializer(product) for product in products]