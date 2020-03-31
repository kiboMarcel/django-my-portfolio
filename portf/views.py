from django.shortcuts import render

# Create your views here.

def homeMe(request):
    return render(request, 'portf/index.html')
