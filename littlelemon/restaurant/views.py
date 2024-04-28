import rest_framework.generics
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemView(rest_framework.generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

#class SingleMenuItemView(rest_framework.generics.RetrieveUpdateDestroyAPIView, rest_framework.generics.DestroyAPIView)

class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer