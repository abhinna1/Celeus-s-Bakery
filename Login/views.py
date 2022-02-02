from django.shortcuts import redirect, render
# from ..Register.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import login, logout, authenticate, get_user_model;
# Create your views here.

def renderLogin(request):
    # logout(request)
    print(request.user.username)
    if(request.method=='POST'):
        username = request.POST['username']
        password =  request.POST['password']
        
        errors = {'usernameEr':'', 'passwordEr':''}
        user=authenticate(request, username=username, password=password)
        if(user is not None):
            login(request, user)
            return redirect('/register')
        else:
            errors['passwordEr'] = 'User not found.'
            return render(request, 'login.html', errors)        
    else:
        return render(request, 'login.html')