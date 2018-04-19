from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.
#-------------------
# RENDER INDEX.HTML
#-------------------
def index(request):
    users = User.objects.all()
    return render(request, "first_app/index.html", {'users': users})
#-------------------
# RENDER EDIT.HTML
#-------------------
def edit(request, id):
    users = User.objects.get(id=id)
    return render(request, "first_app/edit.html", {'users': users})
#-------------------
# RENDER NEW.HTML
#-------------------
def new(request):
    return render(request, "first_app/new.html")
#-------------------
# RENDER SHOW.HTML
#-------------------
def show(request, id):
    show_user = User.objects.get(id = id)
    context = {
        'show_user': show_user
    }
    return render(request, "first_app/show.html", {'show_user': show_user})
#-------------------
# PROCESS
#-------------------
def process(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        add_user = User.objects.create(first_name = firstname, last_name=lastname,email=email)
        add_user.save()
        return redirect('/')
#-------------------
# EDIT USER
#-------------------
def edituser(request, id):
    if request.method == "POST":
        user = User.objects.get(id=id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/')
#-------------------
# DELETE USER
#-------------------
def delete(request, id):
    del_user = User.objects.get(id=id)
    del_user.delete()
    return redirect('/')