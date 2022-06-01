from modeltranslation.translator import register, TranslationOptions
from .models import ProjectModel

@register(ProjectModel)
class ProjectModelTranslationOptions(TranslationOptions):
    fields = ('ProjectName', 'ProjectDesc',)