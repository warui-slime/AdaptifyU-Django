from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Account created for {username}!")
            return redirect('login')
    else:    
        form = UserRegistrationForm()
    return render(request,'users/signup.html',{'form':form})



def logout_user(request):
    logout(request)
    return redirect('homepage')