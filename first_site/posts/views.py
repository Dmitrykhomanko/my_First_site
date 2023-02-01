from django.http import HttpResponse


def index(request):
    return HttpResponse ("Главная сткраница")

def post(request,id):
    return HttpResponse (f"А тут посты {id} ")

def group(request,name):
    return HttpResponse (f"Группа : {name} ")

