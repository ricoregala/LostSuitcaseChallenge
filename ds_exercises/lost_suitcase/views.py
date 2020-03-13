from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>THIS IS A TEST!</h1>')