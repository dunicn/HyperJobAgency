from django.urls import path
from .views import VacanciesView, NewVacancyView


urlpatterns = [

    path('vacancies/', VacanciesView.as_view(), name='vacancies-page'),
    path('vacancy/new', NewVacancyView.as_view(), name='new-vacancy'),
]
