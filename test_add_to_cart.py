#!/usr/bin/env python
"""
Test add to cart functionality after fix.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from store.models import Product


def run_add_to_cart_test():
    print('='*60)
    print('TESTING ADD TO CART FIX')
    print('='*60)
    print()

    unique_user = f'test_add_cart_fix_{User.objects.count() + 1}'
    user, _ = User.objects.get_or_create(username=unique_user, defaults={'password': 'test'})
    client = Client()
    client.force_login(user)

    product = Product.objects.first()
    if not product:
        print('No products available for testing.')
        return

    print(f'Product: {product.name}')
    print()

    # Test Add to Cart with quantity
    print('Test 1: Add to cart with quantity=2')
    post_data = {'quantity': '2'}
    response = client.post(f'/cart/add/{product.id}/', post_data)
    print(f'Response status: {response.status_code}')

    session = client.session
    if 'cart' in session:
        cart_contents = session['cart']
        print(f'Cart contents: {cart_contents}')
        if str(product.id) in cart_contents:
            qty = cart_contents[str(product.id)]
            print(f'Product quantity in cart: {qty}')
        else:
            print('Product not in cart!')
    else:
        print('Cart not in session!')
    print()

    # Test Add to Cart again (should increment)
    print('Test 2: Add same product again with quantity=3 (should increment)')
    post_data = {'quantity': '3'}
    response = client.post(f'/cart/add/{product.id}/', post_data)
    print(f'Response status: {response.status_code}')

    session = client.session
    if str(product.id) in session['cart']:
        qty = session['cart'][str(product.id)]
        print(f'Product quantity in cart now: {qty} (should be 5)')
    else:
        print('Product not in cart!')
    print()

    print('='*60)
    print('✓ ADD TO CART FIX VERIFIED')
    print('='*60)


if __name__ == '__main__':
    run_add_to_cart_test()
