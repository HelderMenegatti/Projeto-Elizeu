from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
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

        username = request.POST['username']
        email = request.POST['email']
        register_form = RegisterForme(request.POST)

        if register_form.is_valid():
            register_form.save()
            
            user = User.objects.get(username=username)
            id = user.id
            user.is_authenticated = False
            user.save()
    
            Rand_token = uuid4()
            Token.objects.create(token=Rand_token, id_user=id)

            send_message(Rand_token, email)

            messages.success(request,"A mensagem de cadastro de senha foi enviada para seu email com sucesso!!!")
            return render(request, 'initial/index.html', {'form':register_form})

        else:
            for error in register_form.errors.values():
                messages.error(request, f'{error}')
                register_form = RegisterForme()

                context = {
                    "form":register_form
                }
                return render(request, "initial/index.html", context)

    elif request.method == "GET":
        request_token = request.GET['token']
        query = Token.objects.filter(token=request_token)
        for q in query:
            tokens = q.token
            if request_token == tokens:
                context = {
                    'token': request_token,
                }
                return render(request, template_name ,context)
        return HttpResponse("não auto", status=401)

    else:
        register_form = RegisterForme()
        template_name = "initial/index.html"
        context = {
            "form":register_form
        }
        return render(request, template_name, context)


def sign_up_password(request):
    template_name = 'initial/login.html'
    if request.method == "POST":
        token = request.POST['name']
        q_token = Token.objects.get(token=token).id_user
        q = User.objects.get(id=q_token)
        print(q.password)
        register_form = SignUpPasswordForme(request.POST)
        if register_form.is_valid():
            q.password = request.POST['password']
            q.save()
            return render(request, template_name)

        return HttpResponse('algo esta errado', status=404)