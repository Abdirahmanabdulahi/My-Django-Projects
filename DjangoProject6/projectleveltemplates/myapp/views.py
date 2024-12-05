from django.shortcuts import render

# Create your views here.
def myindex_view(request):
    return render(request, 'index.html')

def children(request):
    return render (request, "children.html")


def home(request):
    return render (request, "Home.html")

def about(request):
    return render (request, "AboutUs.html")