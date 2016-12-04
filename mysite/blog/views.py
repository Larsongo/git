from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from django.template import loader,Context
from .forms import PlusForm
import time
'''
def index(req):
    t = loader.get_template('index.html')
    c = Context({})
    
    return HttpResponse(t.render(c))
'''
def index(req):
    #user=["lishen"]
    menu_list=["daily_log","daily_study","daily_ent"]
    user={'name':'Larson','sex':'male','age':'26'}
    return render(req,'index.html',{'user':user,'menu_list':menu_list})
def daily_log(req):
    return render(req,'daily_log.html')

def add1(req):
    a = req.GET['a']
    b = req.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))
def add2(req,a,b):
    c = int(a)+int(b)
    return HttpResponse("The SUM of is" + str(c))
    

def plus(req):
    time_t = time.ctime(time.time()) 
    if req.method == 'POST':
        form = PlusForm(req.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse("The sum of A and B is :" + str(int(a)+int(b)))
    else:
        form = PlusForm()
       
    return render(req,'add.html',{'form':form,'time':time_t}) 
