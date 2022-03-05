from django.shortcuts import render
from django.http import HttpResponse
from .models import Dashboards

def principal(request):
	return render(request,'blog/principal.html')

def home(request):
	context = {'Dashboards':Dashboards.objects.all()}
	return render(request, 'blog/home.html',context)

def about(request):
	return render(request, 'blog/about.html',{'title':'About'})



# Create your views here.
