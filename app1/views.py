from django.shortcuts import render

# Create your views here.


def fun1(request):
    d={'name':'shashi','age':24}
    return render(request,'shashi.html',context=d)