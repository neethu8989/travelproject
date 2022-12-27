from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "user is not vallid")
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        emailid = request.POST['email id']
        password1 = request.POST['password']
        password2 = request.POST['password']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            elif User.objects.filter(email=emailid).exists():
                messages.info(request, "emailid exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=firstname,
                                                last_name=lastname, email=emailid)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "password not match")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
