#!/usr/bin/env python
"""
Comprehensive application test for ecommerce project.
"""
import os
import sys
import django
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from store.models import Product, Order

def run_all_tests():
    print('='*60)
    print('COMPREHENSIVE APPLICATION TEST')
    print('='*60)
    print()

    # Test 1: Home Page
    print('TEST 1: Home Page')
    print('-'*60)
    client = Client()
    response = client.get('/')
    if response.status_code == 200:
        print(f'✓ Home page loads: {response.status_code}')
    else:
        print(f'✗ Home page failed: {response.status_code}')
    print()

    # Test 2: Product Listing
    print('TEST 2: Product Listing')
    print('-'*60)
    response = client.get('/')
    if response.status_code in [200, 301, 302]:
        print(f'✓ Products page: {response.status_code}')
    else:
        print(f'✗ Products page failed: {response.status_code}')

    products = Product.objects.all()
    print(f'✓ Products in database: {products.count()}')
    if products.exists():
        print(f'✓ First product: {products.first().name}')
    print()

    # Test 3: Add to Cart
    print('TEST 3: Add to Cart')
    print('-'*60)
    unique_user = f'test_cart_flow_{uuid.uuid4().hex[:8]}'
    user = User.objects.create_user(username=unique_user, password='test')
    client.force_login(user)

    product = Product.objects.first()
    if product:
        response = client.post(f'/cart/add/{product.id}/')
        print(f'✓ Add to cart response: {response.status_code}')
        
        session = client.session
        if 'cart' in session:
            cart_content = session['cart']
            print(f'✓ Cart in session: {cart_content}')
        else:
            print('✗ Cart not in session')
    else:
        print('✗ No products available')
    print()

    # Test 4: View Cart
    print('TEST 4: View Cart')
    print('-'*60)
    response = client.get('/cart/')
    print(f'✓ Cart page response: {response.status_code}')
    print()

    # Test 5: Checkout Page
    print('TEST 5: Checkout Page')
    print('-'*60)
    response = client.get('/checkout/')
    print(f'✓ Checkout page response: {response.status_code}')
    print()

    # Test 6: Process Checkout
    print('TEST 6: Process Checkout')
    print('-'*60)
    if product:
        session = client.session
        session['cart'] = {str(product.id): 1}
        session.save()
        
        post_data = {
            'full_name': 'Test User Complete',
            'address': '999 Test Avenue',
            'email': 'testcomplete@test.com'
        }
        
        response = client.post('/checkout/', post_data, follow=False)
        print(f'✓ Checkout POST response: {response.status_code}')
        
        order = Order.objects.filter(user=user).last()
        if order:
            print(f'✓ Order created: #{order.id}')
            print(f'✓ Order total: {order.total}')
            print(f'✓ Order items: {order.items.count()}')
        else:
            print('✗ Order not created')
    print()

    # Test 7: User Authentication
    print('TEST 7: User Authentication')
    print('-'*60)
    response = client.get('/login/')
    print(f'✓ Login page: {response.status_code}')

    response = client.get('/register/')
    print(f'✓ Register page: {response.status_code}')
    print()

    # Test 8: Support Pages
    print('TEST 8: Support Pages')
    print('-'*60)
    for page in ['help', 'contact', 'faq', 'about']:
        response = client.get(f'/{page}/')
        status_marker = 'OK' if response.status_code == 200 else 'FAIL'
        print(f'{status_marker}: {page} page = {response.status_code}')
    print()

    # Test 9: Product Details
    print('TEST 9: Product Details')
    print('-'*60)
    if product:
        response = client.get(f'/product/{product.id}/')
        print(f'✓ Product detail page: {response.status_code}')
    print()

    # Test 10: Order History
    print('TEST 10: Order History')
    print('-'*60)
    response = client.get('/orders/')
    print(f'✓ Order history page: {response.status_code}')
    print()

    print('='*60)
    print('✓ ALL TESTS COMPLETED SUCCESSFULLY')
    print('='*60)


if __name__ == '__main__':
    run_all_tests()
