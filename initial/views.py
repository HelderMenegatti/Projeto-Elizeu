from django.shortcuts import render


def index(request):
    template_name = "initial/index.html"
    return render(request, template_name)


def sing_up(request):
    template_name = "user/singup.html"
    if request.method == "POST":
        email = request.POST['email']
        print(email)
    return render(request, template_name)