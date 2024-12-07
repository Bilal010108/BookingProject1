from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


class RoomPhotoInline(admin.TabularInline):
   model = RoomPhoto
   extra = 1


class HotelPhotoInline(admin.TabularInline):
   model =HotelPhoto
   extra = 1

@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelPhotoInline,]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Room)
class RoomAdmin(TranslationAdmin):
    inlines = [RoomPhotoInline,]


admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Booking)




