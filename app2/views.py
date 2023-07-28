from django.shortcuts import render

# Create your views here.


def fun2(request):
    d={'name':'vardhan','age':23}
    return render(request,'vardhan.html',context=d)

def fun3(request):

    d={'a':34,'b':545,'c':798}
    return render(request,'conditions.html',context=d)