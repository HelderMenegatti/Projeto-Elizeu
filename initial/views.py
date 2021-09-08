from os import error
from django.db import reset_queries
from django.shortcuts import render
from django.contrib.auth.models import User
from .message.trigger import send_message
from django.http import HttpResponse
from .models import Token
import datetime




def index(request):
    template_name = "initial/index.html"
    return render(request, template_name)


def sign_up(request):
    template_name = "initial/singup.html"
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        token = request.POST['csrfmiddlewaretoken']


        up_token = Token.objects.create(token=token)

        # send_message(up_token)

        # User.objects.create_user(username, email)
    elif request.method == "GET":
        tok = request.GET['token']
        print(">>>>>>>>>> ", tok)
        context = {
            'token': tok,
        }
        return render(request, template_name, context)
    else:
        return HttpResponse("não auto", status=401)




