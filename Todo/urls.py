"""Todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.shortcuts import HttpResponse,render,redirect
def login(request):
    if request.method=="GET":
        print(request.method)
        return render(request,'./templates/login.html')
    else:
        print(request.method)
        u=request.POST.get('user')
        print(u)
        p=request.POST.get('pwd')
        print(p)
        if u=='root' and p=='123123':
            return redirect("/index/")
            # return render(request, './templates/index.html')
        else:
            return  render(request,'./templates/login.html',{'msg':'userID or password fault'})

def index(request):
    # return HttpResponse('index')
    return render(request, './templates/index.html',
                  {
                      'name':'alex',
                      'users':['11','22'],
                      'user_dict':{'k1':'v1','k2':'v2'}
                  }
                  )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('index/', index),

]
