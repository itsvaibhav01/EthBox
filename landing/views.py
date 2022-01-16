from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def landing_page(request):
    print('here')
    return render(request=request,template_name="landing/index.html")