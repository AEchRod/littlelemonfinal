from django.test import TestCase
from littlelemonfinal.littlelemon.restaurant.models import MenuItem


class MenuViewTest(TestCase):
    def setUp(self):
        self.MenuItem1 = MenuItem(title = "Ice Cream", price=80, inventory=100)
