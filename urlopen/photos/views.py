from django.shortcuts import render
from django.http import HttpResponse

import urllib2

# Create your views here.

def retrieve_image(request,url):
    img = urllib2.urlopen(url).read()
    return HttpResponse(img)

def eval_test(request,in_val):
    val = eval(in_val)
    return HttpResponse(val)

