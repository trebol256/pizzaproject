from django.test import TestCase
from .models import Orderrequest
from django.urls import reverse


class OrderrequestModelTest(TestCase):
    
    def setUp(self):
        # Initial setup for testing
        self.order = Orderrequest.objects.create(
            pizzatype='Pepperoni',
            commentorder='Extra Peperoni'
        )
    
    def test_order_creation(self):
        # Verify that the order is created correctly
        self.assertEqual(self.order.pizzatype, 'Pepperoni')
        self.assertEqual(self.order.commentorder, 'Extra Peperoni')

    def test_str_method(self):
        # Verify that the __str__ method returns the correct format
        self.assertEqual(str(self.order), 'Pepperoni - Extra Peperoni')

class OrderRequestViewTest(TestCase):

    def test_order_request_view_get(self):
        # Check the view response for GET
        response = self.client.get(reverse('orders:order_request'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/index.html')

    def test_order_request_view_post(self):
        # Check the view response for POST
        response = self.client.post(reverse('orders:order_request'), {
            'pizzatype': 'Pepperoni',
            'commentorder': 'No onions'
        })
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(Orderrequest.objects.filter(pizzatype='Pepperoni').exists())

    def test_order_table_view(self):
        # Create some orders and check the order table view
        Orderrequest.objects.create(pizzatype='Vegetarian', commentorder='Add olives')
        response = self.client.get(reverse('orders:order_table'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/pendings.html')
        self.assertContains(response, 'Vegetarian')