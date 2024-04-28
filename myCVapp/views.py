from django.shortcuts import render

from myCVapp.models import *
from django.http import FileResponse, Http404, HttpResponse
# Create your views here.

def index(request):
    context ={}
    edu = Education.objects.all()
    context['education'] = edu
    exp = Experience.objects.all()
    context['experience'] = exp
    cert = Certificate.objects.all()
    context['certificate'] = cert
    int = Interest.objects.all()
    context['interest'] = int
    skill = Skill.objects.all()
    context['skill'] = skill
    lang = Language.objects.all()
    context['language'] = lang
    
    context['title']='Mateusz Dzieżok - CV'
    
    return render(request, 'index.html',context)
def about(request):
    context ={}
    context['title']='Mateusz Dzieżok - CV'
    return render(request, 'about.html',context)


