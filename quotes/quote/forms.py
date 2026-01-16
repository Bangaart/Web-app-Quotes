from django import forms

from authors.models import Author
from .models import Tag, Quote


class QuoteAddForm(forms.ModelForm):
    quote = forms.CharField(label='Quote text', max_length=250, required=True)
    tags = forms.ModelMultipleChoiceField(label="Tags", queryset=Tag.objects.all(),
                                          widget=forms.CheckboxSelectMultiple())
    author = forms.ModelChoiceField(label="Author", queryset=Author.objects.all(),
                                    widget=forms.Select(attrs={'size': '5'}))

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']
