from django.test import TestCase
from littlelemonfinal.littlelemon.restaurant.models import MenuItem
from littlelemonfinal.littlelemon.restaurant.serializers import MenuItemSerializer
# Create your tests here.

class MenuViewTest(TestCase):
    def test_get_item(self):
        MenuItem.objects.create(title = "Ice Cream", price=80, inventory=100)
        MenuItem.objects.create(title = "Pizza", price=200, inventory=100)

    def test_getall(self):
        # Retrieve all the Menu objects
        all = MenuItem.objects.all()

        # Serialize the retrieved objects - here you apply the variable with all menu objects as your model to be serialized.
        serializer = MenuItemSerializer(all, many=True)

        # Check if the serialized data equals the response
        self.assertEqual(serializer.data, [
            {'title': 'Ice Cream', 'price': 80, 'inventory': 100},
            {'title': 'Pizza', 'price': 100, 'inventory': 50}
        ])
