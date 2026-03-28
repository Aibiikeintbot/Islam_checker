import django_filters
from django import forms
from django.db import models
from .models import Submission
from .choices import TaskType

class SubmissionFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='filter_search', label='Поиск')
    group_name = django_filters.CharFilter(field_name='group_name', lookup_expr='icontains', label='Группа')
    task_type = django_filters.ChoiceFilter(field_name='task_type', choices=TaskType.choices, label='Тип задания')
    is_ai_generated = django_filters.BooleanFilter(field_name='is_ai_generated', label='Сгенерировано ИИ')
    date_from = django_filters.DateFilter(field_name='created_at', lookup_expr='gte', widget=forms.DateInput(attrs={'type': 'date'}), label='Дата с')
    date_to = django_filters.DateFilter(field_name='created_at', lookup_expr='lte', widget=forms.DateInput(attrs={'type': 'date'}), label='Дата по')

    def filter_search(self, queryset, name, value):
        if value:
            return queryset.filter(
                models.Q(full_name__icontains=value) |
                models.Q(group_name__icontains=value) |
                models.Q(task_description__icontains=value) |
                models.Q(student_code__icontains=value)
            )
        return queryset

    class Meta:
        model = Submission
        fields = ['search', 'group_name', 'task_type', 'is_ai_generated', 'date_from', 'date_to']
