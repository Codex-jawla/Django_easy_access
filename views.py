from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
@login_required(login_url='/login')
def index(request):


    data = Student.objects.all()

    context = {
        'title': 'WebTechnologies'
    }
    return render(request,'index.html',context={'data' : data,'title':context})


@login_required(login_url='/login')
def contact(request):
    context ={
        'title': 'Contact'
    }
    return render(request,'contact.html',context)


@login_required(login_url='/login')
def student(request):
    if request.method=="POST":
        data = request.POST
        name = data.get("username")
        email = data.get("email")
        phone = data.get("phone")
        rollno = data.get("rollno")
        dept = data.get("dept")

        d=Student.objects.filter(email=email)

        if d.exists():
            messages.warning(request, "Email already exists")
            return redirect('student')

        Student.objects.create(
            name = name,
            rollno = rollno,
            branch =dept,
            email = email,
            phone= phone
        )

        return redirect('/')



    context = {
        'title': 'Student'
    }


    return render(request,'student.html',context)


@login_required(login_url='/login')
def about(request):
    context = {
        'title': 'About'
    }
    return render(request,'about.html',context)


@login_required(login_url='/login')
def delete(request , email):
    dataset = Student.objects.get(email=email)
    dataset.delete()
    return redirect('/')


@login_required(login_url='/login')
def update(request , email):
    dataset = Student.objects.get(email=email)
    if request.method=="POST":
        data = request.POST
        name = data.get("username")
        email = data.get("email")
        phone = data.get("phone")
        rollno = data.get("rollno")
        dept = data.get("dept")

        dataset.name =name
        dataset.email =email
        dataset.phone =phone
        dataset.rollno =rollno
        dataset.branch =dept

        dataset.save()

        return redirect('/')



    context = {
        'data': dataset,
        'title' : 'Update'
    }
    return render(request,'update.html',context)

def login_page(request):

    if request.method=="POST":
        username=request.POST.get('email')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.warning(request,"invalid username")
            return redirect("/login")

        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"invalid username or password")
            return redirect("/login")
        else :
            login(request,user)
            return redirect('/')


    return render(request,'login.html')

def signup(request):
    if request.method=="POST":
        fname = request.POST.get("f-name")
        lname = request.POST.get("l-name")
        username = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.warning(request, "Email already exists")
            return redirect('signup')


        user =User.objects.create(
            first_name = fname,
            last_name = lname,
            username =username
        )
        user.set_password(password)
        user.save()

        messages.success(request,"SignUp successful")
        return redirect('login')

    return render(request,'signup.html')

def log_out(request):
    logout(request)
    return redirect('/login')