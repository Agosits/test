# Create your views here.
# coding=utf-8
from django.shortcuts import render_to_response, RequestContext
import datetime
# from django.views.decorators.csrf import csrf_protect
 
# @csrf_protect
def add(request):
    dict={}
    if request.method=="POST":
        comment=request.POST.get('comment','')
        submit_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dict.setdefault('comment',comment)
        dict.setdefault('submit_time',submit_time)
    return render_to_response("add.html",dict,context_instance=RequestContext(request))
