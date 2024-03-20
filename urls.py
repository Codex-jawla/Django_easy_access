
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name ="index"),
    path('contact',contact,name='contact'),
    path('student',student,name='student'),
    path('login',login_page,name='login'),
    path('signup',signup,name='signup'),
    path('logout',log_out,name='logout'),
    path('about',about,name='about'),
    path('fdata',fakedata,name='fake'),
    path('fmarks',marksdata,name='mark'),
    path('stuinfo/<student>',stuInfo,name='info'),
    path('delete/<email>',delete,name='delete'),
    path('update/<email>',update,name='update')
]
