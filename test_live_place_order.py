#!/usr/bin/env python
"""
Test place order via the actual running server.
"""
import re
import uuid
import urllib.request
import urllib.parse
import http.cookiejar

base_url = 'http://localhost:8000'


def run_live_place_order_test():
    print('='*60)
    print('TESTING PLACE ORDER VIA LIVE SERVER')
    print('='*60)
    print()

    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    urllib.request.install_opener(opener)

    username = f'livetest_{uuid.uuid4().hex[:8]}'
    password = 'testpass123'

    print('Step 1: Register user')
    register_data = urllib.parse.urlencode({
        'username': username,
        'password1': password,
        'password2': password,
    }).encode('utf-8')

    try:
        response = urllib.request.urlopen(f'{base_url}/register/', register_data, timeout=5)
        print(f'Register response: {response.status}')
    except urllib.error.HTTPError as e:
        print(f'Register response: {e.code}')
    print()

    print('Step 2: Login')
    login_data = urllib.parse.urlencode({
        'username': username,
        'password': password,
    }).encode('utf-8')

    try:
        response = urllib.request.urlopen(f'{base_url}/login/', login_data, timeout=5)
        print(f'Login response: {response.status}')
    except urllib.error.HTTPError as e:
        print(f'Login response: {e.code}')
    print()

    print('Step 3: Get home page')
    response = urllib.request.urlopen(f'{base_url}/', timeout=5)
    content = response.read().decode('utf-8')
    print(f'Home page response: {response.status}')

    product_matches = re.findall(r'/product/(\d+)/', content)
    if product_matches:
        product_id = product_matches[0]
        print(f'Found product ID: {product_id}')
    else:
        print('No product ID found on the home page.')
        return
    print()

    print('Step 4: Add to cart')
    add_cart_data = urllib.parse.urlencode({'quantity': '1'}).encode('utf-8')
    try:
        response = urllib.request.urlopen(f'{base_url}/cart/add/{product_id}/', add_cart_data, timeout=5)
        print(f'Add to cart response: {response.status}')
    except urllib.error.HTTPError as e:
        print(f'Add to cart response: {e.code}')
    print()

    print('Step 5: View cart')
    response = urllib.request.urlopen(f'{base_url}/cart/', timeout=5)
    print(f'Cart page response: {response.status}')
    print()

    print('Step 6: Load checkout page')
    response = urllib.request.urlopen(f'{base_url}/checkout/', timeout=5)
    checkout_html = response.read().decode('utf-8')
    print(f'Checkout page response: {response.status}')

    csrf_match = re.search(r"csrfmiddlewaretoken['\"]?\s*value['\"]?=\s*['\"]([^'\"]+)['\"]", checkout_html)
    if csrf_match:
        csrf_token = csrf_match.group(1)
        print('Found CSRF token')
    else:
        print('CSRF token not found!')
        csrf_token = None
    print()

    print('Step 7: Place order (submit checkout form)')
    if csrf_token:
        checkout_data = urllib.parse.urlencode({
            'csrfmiddlewaretoken': csrf_token,
            'full_name': 'Test User Live',
            'address': '999 Test Street',
            'email': 'livetest@example.com',
        }).encode('utf-8')

        try:
            response = urllib.request.urlopen(f'{base_url}/checkout/', checkout_data, timeout=5)
            print(f'Place order response: {response.status}')
        except urllib.error.HTTPError as e:
            if e.code == 302:
                print(f'Place order response: {e.code} (redirect)')
            else:
                print(f'Place order response: {e.code}')
                print(f'Error: {e.read().decode("utf-8")[:200]}')
    else:
        print('Cannot place order: no CSRF token')

    print()
    print('='*60)
    print('LIVE SERVER TEST COMPLETE')
    print('='*60)


if __name__ == '__main__':
    try:
        run_live_place_order_test()
    except urllib.error.URLError as e:
        print(f'ERROR: Cannot connect to server - {e}')
        print('Make sure the server is running at http://localhost:8000/')
    except Exception as e:
        print(f'ERROR: {type(e).__name__}: {str(e)}')
        import traceback
        traceback.print_exc()
