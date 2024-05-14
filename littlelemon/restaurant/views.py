import rest_framework.generics
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking, MenuItem
from .serializers import MenuSerializer, BookingSerializer, MenuItemSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemView(rest_framework.generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

#class SingleMenuItemView(rest_framework.generics.RetrieveUpdateDestroyAPIView, rest_framework.generics.DestroyAPIView)
class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class SingleMenuItemView(rest_framework.generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem
    serializer_class = MenuItemSerializer

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return ({"message":"This view is protected"})