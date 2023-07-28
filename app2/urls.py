from django.urls import path

from app2.views import *

urlpatterns=[
    path('fun2/',fun2,name='fun2'),
    path('fun3/',fun3,name='fun3')
]