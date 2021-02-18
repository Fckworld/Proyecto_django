#Request: Realizar peticiones al servidor
#Objeto HTTP Response: Es para enviar la respuesta usando el protocolo HTTP (80)
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to my first page on Django")
