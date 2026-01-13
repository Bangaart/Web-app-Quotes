from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic

from .forms import AddAuthorForm
from .models import Author


# Create your views here.

@login_required
def add(request):
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        form.as_ul()
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect(to='main:main')
    else:
        form = AddAuthorForm()

    return render(request, 'authors/add.html', context={'form': form})


class AuthorsListView(generic.ListView):
    model = Author
    template_name = 'authors/details.html'
    context_object_name = 'authors'

    def get_queryset(self):
        return Author.objects.all()


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'authors/authorPage.html'
    context_object_name = 'author'

    def get_object(self, **kwargs):
        return Author.objects.get(pk=self.kwargs['pk'])
