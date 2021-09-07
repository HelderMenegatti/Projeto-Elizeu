from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    template_name = "initial/index.html"
    return render(request, template_name)


def sign_up(request):
    template_name = "initial/singup.html"
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']
        User.objects.create_user(username, email, password)
    return render(request, template_name)