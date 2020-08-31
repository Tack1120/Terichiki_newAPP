from django.http import HttpResponse
from django.views.generic import ListView    
from django.shortcuts import render

from .forms import UserForm
from .models import VerbModel 
from scripts import tense

def textform(request):
    params = {'sentence': '', 'verbclass1': '', 'verbclass2': '', 'verbclass3': '', 'verbclass4': '', 'verbclass5': '', 'verbclass6': '', 'verbclass7': '', 'verbclass8': '', 'verbclass9': '', 'verbclass10': '','form': None}
    sentence = ""
    if request.method == 'POST':
        form = UserForm(request.POST)
        sentence = request.POST['sentence']
        params['sentence'] = sentence
        params['form'] = form
    else:
        params['form'] = UserForm()

    sentencelist = tense.showtense(sentence)
    for i in range(10):
        params['verbclass' + str(i+1)] = sentencelist[i] 

    return render(request, 'polls/textform.html', params)


class VerbListView(ListView):    
    model = VerbModel  

def helloworld(response):
    return HttpResponse('hello world')
