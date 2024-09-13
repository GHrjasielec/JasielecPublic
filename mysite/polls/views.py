from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. This change has been made to show the difference in someones branches and their commits.")