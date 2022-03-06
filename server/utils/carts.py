from rest_framework import exceptions


def is_the_product_avaiable(product, ammount):
   if product.active and ammount <= product.stok:
      return True
   raise exceptions.ValidationError({'detail': 'Product is not available'})
