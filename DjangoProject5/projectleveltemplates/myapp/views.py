from django.shortcuts import render

# Create your views here.
def myindex_view(request):
    return render(request, 'index.html')

def mychildren_view(request):
    return render (request, "myapp/children.html")


def myhome_view(request):
    return render (request, "myapp/Home.html")