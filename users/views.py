from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from producer.models import Project

@login_required
def project_list(request):
    projects = Project.objects.all()  # Assuming you have a Project model
    return render(request, 'project_list.html', {'projects': projects})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout
