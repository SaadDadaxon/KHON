from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages


def login_views_1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('article:list')
        return render(request, 'account/user404.html')
    return render(request, 'account/login.html')


def login_views(request):
    if not request.user.is_anonymous:
        return redirect('article:list')
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_page = request.GET.get('next')
            if next_page:
                messages.success(request, f'Mr.{request.user} siz Muvaffaqiyatli Kirdingiz')
                return redirect(next_page)
            return redirect('article:list')
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)


def logout_views(request):
    if not request.user.is_authenticated:
        return redirect('account:login')
    if request.method == "POST":
        logout(request)
        messages.success(request, f'Mr.{request.user} siz Muvaffaqiyatli Chiqdingiz')
        return redirect('account:login')
    return render(request, 'account/logout.html')


def register_views(request):
    if request.user.is_authenticated:
        return redirect('article:list')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f"Mr.{request.user} siz Muvaffaqiyatli Ro'yxatdan O'tdingiz")
        return redirect('account:login')
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)






