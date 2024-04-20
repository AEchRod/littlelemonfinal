from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ['menu_id', 'title', 'price', 'inventory']