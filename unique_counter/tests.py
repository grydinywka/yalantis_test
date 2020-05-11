from django.test import TestCase
from django.test import Client


class TestCounter(TestCase):
    def test_visitor(self):
        # create client for http request
        c = Client(HTTP_USER_AGENT='Mozilla/5.0')
        response = c.get('/')
        self.assertIn('You are a new visitor!'.encode(), response.content)
        self.assertIn('The page was visited by 1 customer.'.encode(), response.content)

        response = c.get('/')
        self.assertNotIn('You are a new visitor!'.encode(), response.content)
        self.assertIn('The page was visited by 1 customer.'.encode(), response.content)
        
        # create new client
        c2 = Client(HTTP_USER_AGENT='Mozilla/5.0')
        response = c2.get('/')

        self.assertIn('You are a new visitor!'.encode(), response.content)
        self.assertIn('The page was visited by 2 customers.'.encode(), response.content)

        # try to use first client
        response = c.get('/')
        self.assertNotIn('You are a new visitor!'.encode(), response.content)
        self.assertIn('The page was visited by 2 customers.'.encode(), response.content)

