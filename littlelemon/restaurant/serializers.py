from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking, MenuItem

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['menu_id', 'title', 'price', 'inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ['menuitem_id', 'title', 'price', 'inventory']
