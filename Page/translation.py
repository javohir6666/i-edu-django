from modeltranslation.translator import register, TranslationOptions
from .models import PageModel

@register(PageModel)
class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)