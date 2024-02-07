from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        required=True, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control'
            }
        )
    )

    password1 = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'form-control'
            }
        )
    )

    password2 = forms.CharField(
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
                'class': 'form-control'
            }
        )
    )




class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'book name',
                'class' : 'form-control'
            }
        )
    )

    author = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': "author's name...",
                'class': 'form-control'
            }
        )
    )

    front_page = forms.ImageField(
        required=True,
        widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control'
            }
        )
    )

    description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'description...',
                'class': 'form-control'
            }
        )
    )

    summary = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder' : 'summary...',
                'class':'form-control'
            }
        )
    )

    book_genre = forms.ChoiceField(
        choices=[
            ('Fairytales','Fairytales'),
            ('Historical Fiction', 'Historical Fiction'),
            ('Poetry','Poetry'),
            ('Picture Books','Picture Books')
        ],
        required=True,
        widget=forms.Select(

            attrs={
                'class':'form-control'
            }
        )
    )

    book_code = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'code...', 
                'class':'form-control'
                }
        )
    )

    edition = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'edition...', 
                'class':'form-control'
                }
        )
    )

    length= forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'length..', 
                'class':'form-control'
                }
        )
    )


    chapter = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'chapter...', 
                'class':'form-control'
                }
        )
    )

    publisher = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'publisher...', 
                'class':'form-control'
                }
        )
    )

    published_date = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'placeholder':'date...', 
                'class':'form-control'
                }
        )
    )


    published_in = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'location...', 
                'class':'form-control'
                }
        )
    )


    copies = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder':'copies...', 
                'class':'form-control'
                }
        )
    )

    language = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'language...', 
                'class':'form-control'
                }
        )
    )


    rating = forms.CharField(
            required=True,
            widget=forms.TextInput(
                attrs={
                    'placeholder':'rating...', 
                    'class':'form-control'
                    }
            )
        )
    