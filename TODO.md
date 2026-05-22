# TODO - Simple E-commerce (Django + HTML/CSS/JS)

## Frontend (templates + static)
- [x] base.html
- [x] home.html
- [x] product_detail.html
- [x] cart.html
- [x] checkout.html
- [x] register.html
- [x] login.html
- [x] static/style.css
- [x] static/script.js

## Backend (Django)
- [x] store app models.py (Product, Order, OrderItem)
- [x] store views.py (listing, details, cart, cart actions, auth, checkout)
- [x] store urls.py
- [x] project urls.py includes store.urls
- [x] settings.py (templates + static for development)
- [x] migrations + migrate

## Remaining (to complete requested feature-set)
- [ ] Fix checkout template total vs subtotal if needed
- [ ] Seed sample products for first run (management command or fixture)
- [ ] Ensure cart add/update/remove work for GET/POST consistently
- [ ] Basic tests for views/cart logic
- [ ] Admin registration for Product/Order/OrderItem

