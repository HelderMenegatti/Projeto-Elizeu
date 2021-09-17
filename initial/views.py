from django.contrib import messages 

from django import http
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForme
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
        email_2 = request.POST['email-2']

        register_form = RegisterForme(request.POST)
        if register_form.is_valid():
            register_form.save()
            
            user = User.objects.get(username=username)
            id = user.id
            user.is_active = False
            user.save()
    
            Rand_token = uuid4()
            Token.objects.create(token=Rand_token, id_user=id)

            # send_message(Rand_token, email)

            messages.success(request,"Email enviado com sucesso!!!")
            return render(request, 'initial/index.html', {'form':register_form})
            # return HttpResponse("Emai enviado", status=200)
            # else:
            #     return render(request, "home.html", {'form':RegisterForme})            
            #     # form = RegisterForme(None)   
            #     # return render(request, 'home.html', {'form':form})
            #     # return render(request, 'initial/index.html', {'form': RegisterForme()}) 
        else:
            for error in register_form.errors.values():
                messages.error(request, f'{error}')
                register_form = RegisterForme()

                context = {
                    "form":register_form
                }
                return render(request, "initial/index.html", context)

            # form = RegisterForme()
            # print(">>>>>>>>>>>>>>>>>>> Aqui" )
            # return render(request, 'initial/index.html', {'form':form})

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

