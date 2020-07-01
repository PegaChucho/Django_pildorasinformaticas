from django.http import HttpResponse

def saludo(request): #primera vista
    return HttpResponse("Hola, esta es mi primera página web , la web de Chucho")

def despedida(request): #segunda vista
     return HttpResponse("Hasta luego, compas c:")