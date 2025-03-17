from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record, Book

def home(request):
    records = Record.objects.all()
    
    #check to see if loggin in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authentication
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try again!!")
            return redirect('home')
        
    else:   
        return render(request, 'home.html',{'records':records})
    
def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login 
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have been successfully been registered!")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        #look up record
        customer_record=Record.objects.get(id=pk)
        return render(request, 'record.html',{'customer_record':customer_record})
    else:
        messages.success(request, "Must be logged in to view the page !!")
        return redirect('home')
    
def customer_record(request, pk):
    if request.user.is_authenticated:
        # Lookup record
        customer_record = get_object_or_404(Record, id=pk)
        books = customer_record.books.all()  # Fetch books associated with the record

        if request.method == "POST":
            title = request.POST.get("title")
            author = request.POST.get("author")
            read_date = request.POST.get("read_date")

            if title and author and read_date:
                Book.objects.create(record=customer_record, title=title, author=author, read_date=read_date)
                messages.success(request, "Book added successfully!")
                return redirect('record', pk=customer_record.id)  # Refresh page

        return render(request, 'record.html', {'customer_record': customer_record, 'books': books})

    else:
        messages.error(request, "You must be logged in to view this page!")
        return redirect('home')