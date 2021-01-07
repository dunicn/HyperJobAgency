from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied


class VacanciesView(View):
    def get(self, request, *args, **kwargs):
        context = {'vacancies': Vacancy.objects.all()}
        return render(request, 'vacancy/vacancy.html', context)


class NewVacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vacancy/new_vacancy.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                data = request.POST.get("description")
                Vacancy.objects.create(description=data, author=request.user)
                return redirect('/home')
            else:
                raise PermissionDenied
        else:
            return redirect('/login')
