from django.shortcuts import render

from myCVapp.models import *
from django.http import FileResponse, Http404, HttpResponse
# Create your views here.

def index(request):
    context ={}
    edu = Education.objects.all()
    context['education'] = edu
    exp = Experience.objects.order_by('-end_date')
    context['experience'] = exp
    cert = Certificate.objects.order_by('-date')
    context['certificate'] = cert
    int = Interest.objects.all()
    context['interest'] = int
    skill = Skill.objects.order_by('-level')
    context['skill'] = skill
    lang = Language.objects.all()
    context['language'] = lang
    
    context['title']='Mateusz Dzieżok - CV'
    
    return render(request, 'index.html',context)
def about(request):
    context ={}
    context['title']='Mateusz Dzieżok - CV'
    return render(request, 'about.html',context)


