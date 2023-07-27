from django.shortcuts import render

# Create your views here.


def fun2(request):
    d={'name':'vardhan','age':23}
    return render(request,'vardhan.html',context=d)