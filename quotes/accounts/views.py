from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from .forms import RegisterUser


def signupuser(request):
    if request.user.is_authenticated:
        return redirect('main:main')
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='main:main')
        else:
            return render(request, 'accounts/signup.html', {'form': form})

    return render(request, 'accounts/signup.html', context={'form': RegisterUser()})


class Loginuser(views.LoginView):
    template_name = 'accounts/login.html'
    next_page = '/'
    redirect_authenticated_user = True


class LogoutUser(LoginRequiredMixin, views.LogoutView):
    next_page = '/'
