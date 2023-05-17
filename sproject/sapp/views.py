from django.shortcuts import render, redirect
from . models import Check
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('temporary')
        else:
            return HttpResponse("username or password is incorrect")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password!=cpassword or username is None:
            return HttpResponse("your password is incorrect or username is empty")
            return redirect('register/')

        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
    return render(request,'register.html')



def add_details(request):
    ch = Check.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        materials_provided = request.POST.get('materials')
        account_type = request.POST.get('account_type')
        district = request.POST.get('district')
        branch = request.POST.get('branch')

        tk = Check(name=name, dob=dob, age=age, phone=phone, email=email, address=address, gender=gender, materials_provided=materials_provided, account_type=account_type, district=district, branch=branch)
        tk.save()
        return redirect('redirecting')
    return render(request, 'sample.html', {'ch': ch})

def temporary(request):
    return render(request, 'temp.html')


def redirecting(request):
    return render(request,'direct.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
