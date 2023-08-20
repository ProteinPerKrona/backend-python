def product_serializer(product) -> dict:
    try:
        return {
            'product':str(product['product']),
            'ppk':float(product['ppk']),
            'weight':int(product['weight']),
            'price':int(product['price']),
            'nutritions':{
                'protein':float(product['nutritions']['protein']),
                'fett':float(product['nutritions']['fett']),
                'kolhydrat':float(product['nutritions']['kolhydrat']),
                'varav sockerarter':float(product['nutritions']['varav sockerarter']),


            }
        }
    except Exception as error:
        print(error)
        #print("fail with",product['product'])

        #print(product)

def products_serializer(products) -> list:
    return [product_serializer(product) for product in products]