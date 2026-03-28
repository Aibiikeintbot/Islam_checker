from rest_framework import generics, status
from rest_framework.response import Response
from core.helpers import get_score_color
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Submission
from .serializers import (
    SubmissionCreateSerializer,
    SubmissionListSerializer,
    SubmissionDetailSerializer,
    SubmissionResultSerializer
)
from .filters import SubmissionFilter
from .choices import SubmissionStatus


class SubmissionCreateView(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionCreateSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Отправить задание на проверку",
        operation_description="Создает новое задание",
        request_body=SubmissionCreateSerializer,
        responses={201: SubmissionCreateSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SubmissionListView(generics.ListAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = SubmissionFilter
    search_fields = ['full_name', 'group_name', 'task_description', 'student_code']
    ordering_fields = ['created_at', 'score', 'full_name']
    ordering = ['-created_at']

    @swagger_auto_schema(
        operation_summary="Получить список заданий",
        manual_parameters=[
            openapi.Parameter('search', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('group_name', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('task_type', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('is_ai_generated', openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('date_from', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('date_to', openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SubmissionDetailView(generics.RetrieveAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_summary="Получить детальную информацию",
        responses={200: SubmissionDetailSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SubmissionResultView(generics.RetrieveAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionResultSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_summary="Получить результат проверки",
        responses={200: SubmissionResultSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SubmissionCheckView(generics.GenericAPIView):
    queryset = Submission.objects.all()
    lookup_field = 'id'
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Запустить проверку",
        responses={200: "OK"})
    def post(self, request, *args, **kwargs):
        submission = self.get_object()
        submission.status = SubmissionStatus.PROCESSING
        submission.save()
        return Response({
            "message": "Проверка запущена",
            "submission_id": submission.id
        }, status=status.HTTP_200_OK)