from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_view(requset):
    if requset.method == 'POST':
        username = requset.POST.get('username','')
        password = requset.POST.get('password','')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(requset,user)
            return HttpResponseRedirect("../loggedin/")
        #else:
        #return HttpResponseRedirect("/account/invalid/")
    return render_to_response('login.html',context_instance=RequestContext(requset))

@csrf_protect
def reg_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("../account/login/")
    else:
        form = UserCreationForm()
    return render_to_response("register.html",
                              {'form':form},
                              context_instance=RequestContext(request))
