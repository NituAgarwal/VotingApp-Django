from django.contrib import admin

from .models import Question,Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date','question_text']
	inlines = [ChoiceInline]
	search_fields = ['question_text']
	list_filter = ['pub_date']
	list_display = ['question_text', 'pub_date']

admin.site.register(Question,QuestionAdmin)