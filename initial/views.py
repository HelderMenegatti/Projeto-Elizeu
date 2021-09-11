from os import error
from django import http
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Token
from .message.trigger import send_message
from django.http import HttpResponse
import datetime
from uuid import uuid4




def index(request):
    template_name = "initial/index.html"
    return render(request, template_name)


def sign_up(request):
    template_name = "initial/singup.html"
    if request.method == "POST":
        # user = request.POST
        email = request.POST['email']
        username = request.POST['username']

        User.objects.create_user(username=username, email=email)

        Rand_token = uuid4()
        Token.objects.create(token=Rand_token)

        send_message(Rand_token, email)
        return HttpResponse("Emai enviado", status=200)

    elif request.method == "GET":
        token_1 = request.GET['token']
        query = Token.objects.filter(token=token_1)
        for token in query:
            tokens = token.token
            if token_1 == tokens:
                context = {
                    'token': token_1,
                }
                return render(request, template_name ,context)
        return HttpResponse("não auto", status=401)




