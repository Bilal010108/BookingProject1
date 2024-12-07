from django.urls import path
from .views import *


urlpatterns = [


    path('', HotelListViewSet.as_view({'get':'list','post': 'create'}), name='hotel_list'),
    path('<int:pk>/', HotelDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='hotel_detail'),

    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='userprofile_detail'),


    path('hotel/', HotelViewSet.as_view({'get': 'list', 'post': 'create'}), name='director_list'),
    path('hotel/<int:pk>/', HotelViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='director_detail'),

    path('room/', RoomViewSet.as_view({'get': 'list', 'post': 'create'}), name='actor_list'),
    path('room/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='actor_detail'),

    path('review/', Review.as_view({'get': 'list', 'post': 'create'}), name='history_list'),
    path('review/<int:pk>/', Review.as_view({'get': 'retrieve', 'put': 'update',
                                                  'delete': 'destroy'}), name='history_detail'),


    path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='history_list'),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                  'delete': 'destroy'}), name='history_detail'),

]