from modeltranslation.translator import register, TranslationOptions
from .models import ServiceModel

@register(ServiceModel)
class ServiceModelTranslationOptions(TranslationOptions):
    fields = ('title', 'desc',)