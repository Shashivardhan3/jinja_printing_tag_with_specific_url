from django.shortcuts import render

# Create your views here.


def fun1(request):
    d={'name':'shashi','age':24}
    return render(request,'shashi.html',context=d)


def fun2(request):

    d={'a':234,'b':55,'c':98}
    return render(request,'ifconditions.html',context=d)


def for_loop(request):

    d={'name':'shashi','age':24,'hobbies':['cricket','football','hockey','kabbadi']}
    return render (request,'for_loop.html',context=d)