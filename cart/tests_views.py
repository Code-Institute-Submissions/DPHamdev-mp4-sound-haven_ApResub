from django.test import TestCase, Client
from django.urls import reverse, resolve
from products.models import Product


class TestCartViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_url_response(self):
        """ Test URL response success """
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Test URL is accessible """
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test using correct template """
        response = self.client.get(reverse('view_cart'))
        self.assertTemplateUsed(response, 'cart/cart.html')


class TestAddToCartViews(TestCase):
    """ Class to test the add_to_cart views """

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(pk=1,
                                              name="testproduct",
                                              price=50.00)
        self.quantity = 1
        self.filled_cart = {}

    def test_url_exists(self):
        """ Test view add to cart """
        url = f'/cart/add/{self.product.id}/'
        found = resolve(url)
        self.assertEqual(found.url_name, "add_to_cart")

    def test_can_add_to_cart(self):
        """ Test if a product can be added to cart successfully """
        session = self.client.session
        session['cart'] = self.filled_bag
        session.save()
        post_data = {
            'cart_item': self.product,
            'quantity': int(self.quantity),
            'redirect_url': '/products/1/'
        }
        response = self.client.post('/cart/add/1/', post_data)
        self.assertEqual(response.status_code, 302)
        updated_cart = self.client.session.get('cart')
        self.assertEqual(updated_cart['1'], 1)


class TestAdjustCartViews(TestCase):
    """ Class to test the adjust_cart views """

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(pk=1,
                                              name="testproduct",
                                              price=50.00)
        self.quantity = 1
        self.filled_cart = {'1': 1, '3': 1}

    def test_url_exists(self):
        """ Test view adjust cart """
        url = f'/cart/adjust/{self.product.id}/'
        found = resolve(url)
        self.assertEqual(found.url_name, "adjust_cart")

    def test_can_adjust_cart(self):
        """ Test if the cart can be adjusted successfully """
        session = self.client.session
        session['cart'] = self.filled_bag
        session.save()
        post_data = {
            'cart_item': self.product,
            'quantity': int(self.quantity + 1)
        }
        response = self.client.post('/cart/adjust/1/', post_data)
        self.assertEqual(response.status_code, 302)
        updated_cart = self.client.session.get('cart')
        self.assertEqual(updated_cart['1'], 2)


class TestRemoveFromCartViews(TestCase):
    """ Class to test the remove_from_cart views """

    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(pk=1,
                                              name="testproduct",
                                              price=50.00)
        self.filled_cart = {'1': 1, '2': 1}

    def test_url_exists(self):
        """ Test view adjust cart """
        url = f'/cart/remove/{self.product.id}/'
        found = resolve(url)
        self.assertEqual(found.url_name, "remove_from_cart")

    def test_can_remove_from_cart(self):
        """ Test if the item can be successfully removed from cart"""
        session = self.client.session
        session['cart'] = self.filled_cart
        session.save()
        response = self.client.post('/cart/remove/1/')
        self.assertEqual(response.status_code, 200)
        updated_cart = self.client.session.get('cart')
        self.assertEqual(len(updated_cart), 1)
