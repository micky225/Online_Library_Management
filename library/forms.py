from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-text'})
        self.fields['email'].widget.attrs.update({'class': 'input-text'})
        self.fields['password1'].widget.attrs.update({'class': 'input-text'})
        self.fields['password2'].widget.attrs.update({'class': 'input-text'})



class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['front_page'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['summary'].widget.attrs.update({'class': 'form-control'})
        self.fields['book_genre'].widget.attrs.update({'class': 'form-control'})
        self.fields['book_code'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['edition'].widget.attrs.update({'class': 'form-control'})
        self.fields['length'].widget.attrs.update({'class': 'form-control'})
        self.fields['chapter'].widget.attrs.update({'class': 'form-control'})
        self.fields['publisher'].widget.attrs.update({'class': 'form-control'})
        self.fields['published_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['published_in'].widget.attrs.update({'class': 'form-control'})
        self.fields['copies'].widget.attrs.update({'class': 'form-control'})
        self.fields['language'].widget.attrs.update({'class': 'form-control'})
        self.fields['rating'].widget.attrs.update({'class': 'form-control'})   