from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import User
from django.contrib.auth import get_user_model



def signup(request):
    User = get_user_model()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
            username=form.cleaned_data["username"],
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
            name=form.cleaned_data["name"]    
            )
            return redirect("accounts:signup")
    else:  
        form = SignUpForm()       
    return render(request, "accounts/signup.html", {"form": form})