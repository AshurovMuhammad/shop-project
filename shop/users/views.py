from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    context = {
        'title': "Tizizmga kirish",
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz☻")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {
        'title': "Ro'yxatdan o'tish",
        'form': form,
    }
    return render(request, 'users/register.html', context=context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Profile',
        'form': form,
    }
    return render(request, 'users/profile.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect('index')


