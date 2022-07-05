from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import Contact
from django.contrib import messages
from myapp.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    messages.error(request, 'this is about')
    return render(request, 'home/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        messages.success(request, 'Your form has been submited')

    return render(request, 'home/contact.html')



def search(request):
    query = request.GET['query']
    if len(query)>100:
        posts = []
    else:
        postsTitle = Post.objects.filter(title__icontains=query)
        postsContent = Post.objects.filter(content__icontains=query)
        postsAuthor = Post.objects.filter(content__icontains=query)
        posts = postsTitle.union(postsContent)

    if posts.count()==0:
        messages.warning(request, 'Your search result does not match with any documents')
    context = {'posts':posts, 'query':query}
    return render(request, 'home/search.html', context)



def signuphandle(request):
    if request.method=="POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')


        if len(username)>10:
            messages.error(request, 'Username must be under 10 charecters')
            return redirect('home')
        if not username.isalnum :
            messages.error(request, 'Username only contains letters and numbers')
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, 'Your password do not match')
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your Vik star id has been successfully created')
        return redirect('home')
    else:
        return HttpResponse("404 - Not Found")


def loginhandle(request):
    if request.method == "POST":
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

    user = authenticate(username=loginusername, password=loginpassword)
    
    if user is not None:
        login(request, user)
        messages.success(request, 'You are successfully logged in')
        return redirect('home')
    else:
        messages.error(request, 'Invalid credentials, Please try again')
        return redirect('home')

    return HttpResponse("404 - Not Found")


def logouthandle(request):
    logout(request)
    messages.success(request, 'Successfully logout')
    return redirect('home')




