from contextvars import Context
from email import contentmanager
from multiprocessing import Value, context
from re import M, template
import re
from urllib import request
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponsePermanentRedirect
import playground
from .models import project
from django.urls import reverse
from  .forms import projectForm


# Create your views here.
def Home(request):
    return HttpResponsePermanentRedirect(reverse('firsttemplate'))

def Project(request):
    return HttpResponsePermanentRedirect(reverse('myfirst'))    

def firsttemplate(request):
    template = loader.get_template('playground/firsttemplate.html')
    return HttpResponse(template.render())



def myfirst(request):
    playground = project.objects.all()
    context = {
        'playground': playground,
    }
    return render(request, "playground/myfirst.html", context)

def Project(request, pk):
    projectobj = project.objects.get(id=pk)
    #tags = projectobj.tags.all()
    #reviews = projectobj.review_set.all()
    context = {'project': projectobj,} #'tags': tags, 'reviews': reviews}
    return render(request, "playground/single-project.html", context)  


def createproject(request):
    form = projectForm()

    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('Project')

    context = {'form': form}
    return render(request, 'playground/project-form.html', context) 
    
def updateproject(request, pk):
    Project = project.objects.get(id=pk)
    form = projectForm(instance=Project)
    if request.method == 'POST':
        form = projectForm(request.POST, request.FILES, instance=Project)
        if form.is_valid():
            form.save()
            return redirect('Project')
    context = {'form':form}
    return render(request, 'playground/project-form.html', context)  

def deleteproject(request, pk):
    Project = project.objects.get(id=pk)
    if request.method == "POST":
        Project.delete()
        return redirect('Project')
    context = {'object': Project}        
    return render(request, 'playground/delete.html', context)    