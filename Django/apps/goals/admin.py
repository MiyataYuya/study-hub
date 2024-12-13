from django.contrib import admin
from .models import StudyGoal

@admin.register(StudyGoal)
class StudyGoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'start_date', 'end_date', 'is_completed')
    search_fields = ('title',)
    list_filter = ('is_completed', 'start_date')