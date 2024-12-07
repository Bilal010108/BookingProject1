from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields =['age','status','phone_number']







class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'



class HotelPhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelPhoto
        fields = '__all__'



class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model =Room
        fields = '__all__'


class RoomPhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomPhoto
        fields = '__all__'



class  ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Review
        fields = '__all__'




class  BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Booking
        fields = '__all__'


class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_room = RoomSerializers(read_only=True, many=True)
    hotel_image = HotelPhotoSerializers(read_only=True, many=True)
    created_date = serializers.DateTimeField(format='%d-%m-%Y')
    class Meta:
        model = Hotel
        fields = ['hotel_image', 'hotel_room','created_date','description','hotel_name']



class HotelListSerializer(serializers.ModelSerializer):
    hotel_image = HotelPhotoSerializers(read_only=True, many=True)
    created_date = serializers.DateTimeField(format='%d-%m-%Y')


    class Meta:
        model = Hotel
        fields = ['hotel_image', 'description', 'hotel_name','hotel_owner','created_date']
