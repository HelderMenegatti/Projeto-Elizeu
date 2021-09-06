from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    template_name = "initial/index.html"
    return render(request, template_name)


def sign_up(request):
    template_name = "user/singup.html"
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']
        print("O EMAIL ENVIADO FOI", email)
        print("O username é", username)
        print("A senha enviada foi", password)

        user = User.objects.create_user(username, email, password)
        print(user)
        print(user)
        print(user)
        print(user)
        print(user)
    return render(request, template_name)