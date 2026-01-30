from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello you are at films index')

def films(request):
    return render(request, 'films.html' , context={"products": films})