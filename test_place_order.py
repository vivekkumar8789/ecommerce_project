#!/usr/bin/env python
"""
Test place order functionality in detail.
"""
import os
import django
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from store.models import Product, Order


def run_place_order_test():
    print('='*60)
    print('DETAILED PLACE ORDER TEST')
    print('='*60)
    print()

    unique_user = f'test_place_order_{uuid.uuid4().hex[:8]}'
    user = User.objects.create_user(username=unique_user, password='test')
    client = Client()
    client.force_login(user)

    product = Product.objects.first()
    if not product:
        print('No products available for testing.')
        return

    print(f'Product: {product.name} - Price: {product.price}')
    print()

    print('Step 1: Adding product to cart')
    response = client.post(f'/cart/add/{product.id}/', {'quantity': '1'})
    print(f'Add to cart response: {response.status_code}')

    session = client.session
    cart_data = session.get('cart', {})
    print(f'Cart contents: {cart_data}')
    print()

    print('Step 2: Verifying cart contents')
    response = client.get('/cart/')
    print(f'Cart view response: {response.status_code}')

    if response.context:
        cart_items = response.context.get('cart_items', [])
        subtotal = response.context.get('subtotal', 0)
        print(f'Cart items in template: {len(cart_items)}')
        print(f'Subtotal: {subtotal}')
    print()

    print('Step 3: Loading checkout page')
    response = client.get('/checkout/', follow=False)
    print(f'Checkout GET response: {response.status_code}')

    if response.status_code == 200:
        if response.context:
            print(f'Context keys: {list(response.context.keys())}')
            form = response.context.get('form')
            if form:
                print(f'Form fields: {list(form.fields.keys())}')
        else:
            print('No context in response')
    elif response.status_code == 302:
        print(f'Redirect to: {response.url}')
    print()

    print('Step 4: Attempting to place order')
    session = client.session
    session['cart'] = {str(product.id): 1}
    session.save()

    post_data = {
        'full_name': 'John Test User',
        'address': '123 Main Street, City',
        'email': 'johntest@example.com'
    }

    try:
        response = client.post('/checkout/', post_data, follow=False)
        print(f'Checkout POST response: {response.status_code}')

        if response.status_code == 302:
            print(f'Redirected to: {response.url}')
            print('Order placed successfully!')

            order = Order.objects.filter(user=user).last()
            if order:
                print(f'Order created: #{order.id}')
                print(f'Total: {order.total}')
                print(f'Status: {order.status}')
                print(f'Items: {order.items.count()}')
            else:
                print('Order not found in database')
        elif response.status_code == 200:
            print('Checkout form returned (validation error)')
            if response.context:
                form = response.context.get('form')
                if form and form.errors:
                    print(f'Form errors: {form.errors}')
        else:
            print(f'Unexpected status: {response.status_code}')

    except Exception as e:
        print(f'Error during checkout: {type(e).__name__}: {str(e)}')
        import traceback
        traceback.print_exc()

    print()
    print('='*60)


if __name__ == '__main__':
    run_place_order_test()
