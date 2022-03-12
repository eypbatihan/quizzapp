from dataclasses import fields
from django.contrib import admin

from .models import Answer, Category, Questions, Quiz

# Register your models here.
class AnswerInline(admin.TabularInline):
    model = Answer
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Quiz)
admin.site.register(Category)
admin.site.register(Answer)
admin.site.register(Questions,QuestionAdmin)
