from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from users.forms import UserRegistrationForm


def home(request):

    return render(request, 'users/home.html')

def register(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password'])

            user.save()

            login(request, user)
            return redirect('home')

    else:

        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})

def login_view(request):

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)
            return redirect('home')

    else:

        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):

    if request.method == 'POST':

        logout(request)

        return redirect('home')

    else:
        return render(request, 'users/logout.html')
