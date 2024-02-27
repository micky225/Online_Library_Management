from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AddBookForm
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.

def home(request):
    return render(request, 'index.html')

@csrf_exempt
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

@csrf_exempt
def singleCourse(request, pk):
    singles = Book.objects.get(pk=pk)
    return render(request, 'single-book.html',{'singles':singles})

@csrf_exempt
def addBook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course')
    else:
        form = AddBookForm() 

    return render(request, 'addbook.html', {'form':form})



@csrf_exempt
def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})            



@csrf_exempt
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




@csrf_exempt
def signOut(request):
    logout(request)
    return redirect('login')    


@csrf_exempt
def delete(request, pk):
    delete = Book.objects.get(pk=pk)

    if request.method == "POST":
        delete.delete()
        return redirect('course')
    return render(request, 'delete.html', {'delete':delete})


class BookAPIView(APIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


    def get(self, request, format=None):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()
            return Response(book.data, status=status.HTTP_201_CREATED)
        return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)



class EditAPIView(APIView):
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)

        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 


    def get(self,  request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response (serializer.data)


    def put(self, request, pk):
        book         = self.get_object(pk)

        serializer   = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)



    def delete(self, request, pk):
        deleteBook = self.get_object(pk)
        if deleteBook:
            deleteBook.delete()
            return Response( status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)



