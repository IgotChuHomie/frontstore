from django.shortcuts import render
from django.http import HttpResponse 



#Simple request handler 
'''
def say_hello(request) :
    return HttpResponse("hello world")
'''


#simple request handler using templates 
def say_hello(request) :
    return render(request,'hello.html',{'name':'oussama'})
