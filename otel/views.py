from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, status, generics
from .models import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers



class HotelViewSet(viewsets.ModelViewSet):
    queryset =Hotel.objects.all()
    serializer_class =HotelSerializers


class HotelPhotoViewSet(viewsets.ModelViewSet):
    queryset =HotelPhoto.objects.all()
    serializer_class =HotelPhotoSerializers



class RoomViewSet(viewsets.ModelViewSet):
    queryset =Room.objects.all()
    serializer_class = RoomSerializers



class RoomPhotoViewSet(viewsets.ModelViewSet):
    queryset =RoomPhoto.objects.all()
    serializer_class =RoomSerializers



class Review (viewsets.ModelViewSet):
    queryset = Review .objects.all()
    serializer_class =ReviewSerializers




class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers




class HotelListViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer




class HotelDetailViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer

