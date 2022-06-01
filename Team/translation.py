from modeltranslation.translator import register, TranslationOptions
from .models import TeamCategory, Worker

@register(TeamCategory)
class TeamCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'desc',)

@register(Worker)
class WorkerTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'desc',)