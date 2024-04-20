import rest_framework.generics
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu
from .serializers import MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemView(rest_framework.generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

#class SingleMenuItemView(rest_framework.generics.RetrieveUpdateDestroyAPIView, rest_framework.generics.DestroyAPIView)
