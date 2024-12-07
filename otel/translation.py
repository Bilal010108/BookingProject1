from modeltranslation.translator import TranslationOptions,register
from .models import Hotel,Room


@register(Hotel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'description')


@register(Room)
class ProductTranslationOptions(TranslationOptions):
    fields = (  'description',)