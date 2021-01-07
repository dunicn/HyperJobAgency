from django.urls import path
from .views import ResumesView, NewResumeView


urlpatterns = [
    path('resumes/', ResumesView.as_view(), name='resumes-page'),
    path('resume/new', NewResumeView.as_view(), name='new-resume'),
]
