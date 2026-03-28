from django.contrib import admin
from django.utils.html import format_html
from .models import Submission


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):

    list_display = (
        'id','full_name','group_name','task_type',
        'score','colored_score','short_comment',
        'status','is_ai_generated','created_at'
    )

    list_filter = ('status','task_type','is_ai_generated')

    list_editable = ('score','short_comment','status')


    def colored_score(self, obj):
        if obj.score is None:
            return "-"

        color = "green" if obj.score >= 85 else "orange" if obj.score >= 60 else "red"

        return format_html(
            '<span style="color:{}; font-weight:bold;">{}</span>',
            color,
            obj.score
        )

    colored_score.short_description = "Оценка"
