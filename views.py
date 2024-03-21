import random
from django.contrib.auth import authenticate , login , logout
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from faker import Faker


# Create your views here.
@login_required(login_url='/login')
def index(request):
    data = Student.objects.all().order_by('rollno')


    if request.GET.get('search'):
        search = request.GET.get('search')
        data=data.filter(
            Q(name__icontains = search)|
            Q(email__icontains=search) |
            Q(branch__icontains=search) |
            Q(phone__icontains = search)
        )

    paginator = Paginator(data, 10)
    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'WebTechnologies'
    }
    return render(request,'index.html',context={'data' : page_obj,'title':context })


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
    context = {

        'title': 'Login'
    }

    return render(request,'login.html',context)

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
    context = {
        'title': 'SignUp'
    }
    return render(request,'signup.html',context)

def log_out(request):
    logout(request)
    return redirect('/login')

myfake = Faker()
def fakedata(request)-> None:

    for i in range(10):
        num = random.randint(0,5)
        name=myfake.name()
        rollno=random.randint(0,120)
        email=myfake.email()
        phone=random.randint(6800000000,9999999999)
        l=["CSE","IT","CST","ECE","ITE","EEE"]
        dept=l[num]

        try:
            Student.objects.create(
                name=name,
                rollno=rollno,
                branch=dept,
                email=email,
                phone=phone
            )
        except Exception as e:

            messages.error(request, f"error : {e}")
            return redirect('/')

    return redirect('/')

def marksdata(request)-> None:

    try:
        stu_det =Student.objects.all()
        for s in stu_det:
            sub_det = Subject.objects.all()
            for sub in sub_det:
                student_Marks.objects.create(
                    student=s,
                    subject=sub,
                    marks = random.randint(15,100)
                )


    except Exception as e:
        print(e)


    return redirect('/')


def stuInfo(request,student):

    dataset = student_Marks.objects.filter(student__email=student)

    context ={
        'data':dataset,
        'title' : "Info"
    }
    return render(request,"stuInfo.html",context)