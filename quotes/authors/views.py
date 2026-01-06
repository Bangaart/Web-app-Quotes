from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import AddAuthorForm


# Create your views here.

@login_required
def add(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(to='main:main')
    else:
        form = AddAuthorForm()

    return render(request, 'authors/add.html', context={'form': form})
