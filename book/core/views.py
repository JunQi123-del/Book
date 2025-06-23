from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#A view is a function that returns a response(HTML,JSON,etc) when someone visits a certail URL
def home(request):
    print(f"The resquest from views.py is: {request}")
    return render(request,'book/home.html')
