from django.contrib import messages
from django.forms.utils import pretty_name 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import *
from .models import PreUser
from .message.trigger import send_message
from django.http import HttpResponse
import datetime
from uuid import uuid4


def sign_up(request):
    template_name = "initial/index.html"

    if request.method == "GET":
        register_form = PreUserForme()

        return render(request, template_name, {'form':register_form})
        
    elif request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        register_form = PreUserForme(request.POST)

        if register_form.is_valid():
            register_form.save()

            Rand_token = uuid4()
            user = PreUser.objects.get(username=username)
            user.token = Rand_token
            user.save()

            send_message(Rand_token, email) 

            messages.success(request,"A mensagem de cadastro de senha foi enviada para seu email com sucesso!!!")
            return redirect('registro')

        else:
            for error in register_form.errors.values():
                messages.error(request, f'{error}')
                register_form = PreUserForme()

                context = {
                    "form":register_form
                }
                return render(request, "initial/index.html", context)
    else:
        register_form = PreUserForme()
        template_name = "initial/index.html"
        context = {
            "form":register_form
        }
        return render(request, template_name, context)





def sign_up_password(request):
    template_name = 'initial/singup.html'

    if request.method == "GET":
        request_token = request.GET['token']
        query = PreUser.objects.get(token=request_token)
        if request_token == query.token:
            context = {
                'token': request_token,
                'user': query
            }
            return render(request, template_name ,context)
        return HttpResponse("não auto", status=401)


    elif request.method == "POST":

        user = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']
        
        register_form = SignUpPasswordForme(request.POST)
        
        if register_form.is_valid():

            User.objects.create_user(username=user, email=email, password=password, is_active=False)
            PreUser.objects.get(username=user).delete()

            messages.success(request,"Cadastro realizado com sucesso!!!")
            return redirect('login')
        else:
            for error in register_form.errors.values():
                messages.error(request, f'{error}')
                register_form = PreUserForme()
                query = PreUser.objects.get(username=user)
                context = {
                    "form":register_form,
                    'user': query
                }
                return render(request, "initial/singup.html", context)
    else:
        register_form = PreUserForme()
        template_name = "initial/index.html"
        context = {
            "form":register_form
        }
        return render(request, template_name, context)



def login(request):
    template_name = 'initial/login.html'
    return render(request, template_name)