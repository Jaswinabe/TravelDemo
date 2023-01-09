from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1 = Team.objects.all()
    return render(request,"index.html",{'result':obj,'ressultt':obj1})

#def arithameticop(request):
  #  x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
    #sum=x+y
    #difference=x-y
    #product=x*y
    #quotient=x/y
    #return render(request,"about.html",{'result':sum,'value':difference,'mul':product,'quo':quotient})



