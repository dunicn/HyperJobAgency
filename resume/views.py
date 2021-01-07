from django.shortcuts import render, redirect
from django.views import View
from .models import Resume
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied


class ResumesView(View):
    def get(self, request, *args, **kwargs):
        context = {'resumes': Resume.objects.all()}
        return render(request, 'resume/resume.html', context)


class NewResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resume/new_resume.html')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if not request.user.is_staff:
                data = request.POST.get("description")
                Resume.objects.create(description=data, author=request.user)
                return redirect('/home')
            else:
                raise PermissionDenied
        else:
            return redirect('/login')
    # def post(self, request, *args, **kwargs):
    #     try:
    #         if request.user.is_authenticated and not User.is_staff:
    #             resume = Resume.objects.create(
    #                 description=request.POST.get("description"),
    #                 author=request.user
    #             )
    #             return redirect("/home")
    #     except Exception:
    #         raise HttpResponseForbidden
