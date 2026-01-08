from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic

from quote.forms import QuoteAddForm
from quote.models import Quote


# Create your views here.

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteAddForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            form.save_m2m()
            return redirect(to='main:main')
        else:
            form = QuoteAddForm()
            return render(request, 'quote/add_quote.html', {'form': form})
    return render(request, 'quote/add_quote.html', {'form': QuoteAddForm()})


class QuoteListView(generic.ListView):
    model = Quote
    template_name = 'quote/quote_list.html'
    context_object_name = 'quote_list'

    def get_queryset(self):
        return Quote.objects.all()
