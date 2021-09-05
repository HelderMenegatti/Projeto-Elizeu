from django.shortcuts import render

def sing_up(request):
    template_name = "user/singup.html"
    return render(request, template_name)
