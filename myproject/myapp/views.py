from django.shortcuts import render,redirect
from myapp.forms import Insert,Signup
from myapp.models import Student
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def insert(request):
    forms=Insert()
    if request.method=='POST':
        form=Insert(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'myapp/insert.html',{'form':forms})

def show(request):
    data=Student.objects.all()
    return render(request,'myapp/show.html',{'data':data})

def delete(request,id):
    data=Student.objects.get(id=id)
    data.delete()
    return redirect('/show')
def update(request,id):
    data = Student.objects.get(id=id)
    if request.method=="POST":
        form=Insert(request.POST,instance=data)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/show')

    return render(request, 'myapp/update.html',{'data':data})

def signup(request):
    form=Signup()
    if request.method=='POST':
      form1=Signup(request.POST)
      if form1.is_valid():
        user=form1.save(commit=True)
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'myapp/signup.html',{'form':form})

def logout(request):
    return render(request,'myapp/logout.html')






