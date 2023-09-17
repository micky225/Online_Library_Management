from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AddBookForm
# Create your views here.

def home(request):
    return render(request, 'index.html')


def course(request):
    books = Book.objects.all()
    search = request.GET.get('keywords')
    if search:
        books=Book.objects.filter(name__icontains=search)
    else:
        books =Book.objects.all()
        search = ""   
    return render(request, 'book.html',{'books':books, 'search': search})



def contact(request):
    return render(request, 'contact.html')        


def singleCourse(request, pk):
    singles = Book.objects.get(pk=pk)
    return render(request, 'single-book.html',{'singles':singles})


def addBook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course')
    else:
        form = AddBookForm() 

    return render(request, 'addbook.html', {'form':form})


def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})            


def signIn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')

    return render(request, 'signin.html')



def signOut(request):
    logout(request)
    return redirect('login')    



def delete(request, pk):
    delete = Book.objects.get(pk=pk)

    if request.method == "POST":
        delete.delete()
        return redirect('course')
    return render(request, 'delete.html', {'delete':delete})