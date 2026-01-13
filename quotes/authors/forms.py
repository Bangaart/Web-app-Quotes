from django import forms

from authors.models import Author


class AddAuthorForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name', max_length=100, required=True)
    born_date = forms.DateField(label='Born Date', required=True,
                                widget=forms.DateInput(
                                    attrs={'input_type': 'date', 'placeholder': "e.g., March 15, 1995"}),
                                error_messages=
                                {'required': "This field can't be blank",
                                 'invalid': 'Please enter a valid date format. Like March 15, 1995'}, )
    born_location = forms.CharField(label='Born Location', max_length=100, required=True)
    description = forms.CharField(label='Description', max_length=500, required=True, widget=forms.Textarea())

    class Meta:
        model = Author
        fields = ['full_name', 'born_date', 'born_location', 'description']
