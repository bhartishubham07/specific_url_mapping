from django.shortcuts import render

# Create your views here.
def asus(request):
    return render(request, 'asus.html')

def acer(request):
    return render(request, 'acer.html')