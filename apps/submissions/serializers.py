from rest_framework import serializers
from core.helpers import get_score_color
from .models import Submission
from .choices import TaskType, SubmissionStatus


class SubmissionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'full_name', 'group_name', 'task_type', 'task_description', 'student_code', 'created_at']
        read_only_fields = ['id', 'created_at']


class SubmissionListSerializer(serializers.ModelSerializer):
    task_type_display = serializers.CharField(source='get_task_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    score_color = serializers.SerializerMethodField()

    class Meta:
        model = Submission
        fields = [
            'id', 'full_name', 'group_name', 'task_type', 'task_type_display',
            'score', 'short_comment', 'status', 'status_display', 'score_color', 'created_at'
        ]

    def get_score_color(self, obj):
        if obj.score is None:
            return 'gray'
        if obj.score >= 85:
            return 'green'
        elif obj.score >= 60:
            return 'orange'
        return 'red'


class SubmissionDetailSerializer(serializers.ModelSerializer):
    task_type_display = serializers.CharField(source='get_task_type_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Submission
        fields = '__all__'


class SubmissionResultSerializer(serializers.ModelSerializer):
    score_color = serializers.SerializerMethodField()

    class Meta:
        model = Submission
        fields = ['id', 'score', 'ai_feedback', 'short_comment', 'is_ai_generated', 'status', 'score_color']

    def get_score_color(self, obj):
        if obj.score is None:
            return 'gray'
        if obj.score >= 85:
            return 'green'
        elif obj.score >= 60:
            return 'orange'
        return 'red'
