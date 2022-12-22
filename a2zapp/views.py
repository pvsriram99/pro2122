from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from a2zapp.forms import empform, newsform, calenderform
from a2zapp.models import empmodel, news, calender

# Create your views here.
def base(request):
    return render(request, 'a2zapp/base.html')
def home(request):
    return render(request, 'a2zapp/home.html')
@login_required
def hrman(request):
    return render(request, 'a2zapp/hrmanager.html')
def emp(request):
    return render(request, 'a2zapp/employee.html')
def empfrm(request):
    form = empform
    if request.method == "POST":
        form = empform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/empdata')
    return render(request, 'a2zapp/empform.html',{'form': form})
def empdata(request):
    data = empmodel.objects.all()
    return render(request, 'a2zapp/empdata.html', {'data': data})
def delete(request,id):
	employee=empmodel.objects.get(id=id)
	employee.delete()
	return redirect('/empdata')

def update(request, id):
    employee = empmodel.objects.get(id=id)
    if request.method=="POST":
        form=empform(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/empdata')
    return render(request, 'a2zapp/update.html',{'employee': employee})

def newsfrm(request):
    data=newsform
    if request.method=="POST":
        form=newsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/latestnews')
    return render(request, 'a2zapp/addnews.html', {'form': data})
def latestnews(request):
    form=news.objects.all()
    return render(request, 'a2zapp/latestnews.html', {'form': form})
def calfrm(request):
    data=calenderform
    if request.method=="POST":
        form=calenderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/holcal')
    return render(request, 'a2zapp/addholidays.html', {'form': data})
def holcal(request):
    hol=calender.objects.all()
    return render(request, 'a2zapp/holidaycalender.html', {'key': hol})
