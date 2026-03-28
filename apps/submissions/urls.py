from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubmissionCreateView.as_view(), name='submission-create'),
    path('list/', views.SubmissionListView.as_view(), name='submission-list'),
    path('<int:id>/', views.SubmissionDetailView.as_view(), name='submission-detail'),
    path('<int:id>/result/', views.SubmissionResultView.as_view(), name='submission-result'),
    path('<int:id>/check/', views.SubmissionCheckView.as_view(), name='submission-check'),
]
