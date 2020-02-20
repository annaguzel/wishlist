from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, SigninForm, WishForm, ListForm
from .models import Wish,List
from django.contrib import messages
import uuid

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("list")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)


def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)

def signout(request):
    logout(request)
    return redirect("list")

def list(request):
    lists=List.objects.all()
    context={
    'lists': lists
    }
    return render(request,"list.html",context)

def wish_list(request, list_id):
    list = List.objects.get(id=list_id)
    wishes=Wish.objects.all().order_by('-pk')
    context = {
        "list": list,
        "wishes": wishes,
    }
    return render(request, 'wish_list.html', context)

def list_create(request):
    if request.user.is_anonymous:
        return redirect("signin")
    form = ListForm()
    if request.method == "POST":
        form = ListForm(request.POST, request.FILES or None)
        if form.is_valid():
            list=form.save(commit=False)
            list.creator = request.user
            list.save()
            #messages.success(request,"List is successfully created!")
            return redirect('list')
        print (form.errors)
    context = {
    "form": form,
    }
    return render(request, 'createlist.html', context)

def wish_create(request, list_id):
    list = List.objects.get(id=list_id)
    if request.user.is_anonymous:
        return redirect('signin')
    #if request.user != list.creator:
    #    return redirect('wish-list',list_id)
    form = WishForm()

    if request.method == "POST":
        form = WishForm(request.POST,request.FILES)
        if form.is_valid():
            wish = form.save(commit=False)
            wish.list = list
            wish.save()
            #messages.success(request,"Your wish is added successfully!")
            return redirect('wish-list', list_id)
    context = {
        "form": form,
        "list":list,
        }
    return render(request, 'wish_create.html', context)

def list_delete(request, list_id):
    List.objects.get(id=list_id).delete()
    return redirect('list')

def wish_delete(request,list_id,wish_id):
    wish=Wish.objects.get(id=wish_id)
    list=wish.list
    if request.user == list.creator:
        wish.delete()
    return redirect('wish-list',wish.list.id)

def wish_purchased(request, list_id, wish_id):
    wish = Wish.objects.get(id=wish_id)
    wish.is_purchased = True
    if request.user.is_authenticated:
        wish.purchased_by = request.user.username
    else :
        wish.purchased_by = "Anonymous"
    wish.save()
    return redirect('wish-list',wish.list.id)

def wish_unpurchased(request, list_id, wish_id):
    wish = Wish.objects.get(id=wish_id)
    wish.is_purchased = False
    wish.save()
    return redirect('wish-list', wish.list.id)




# Create your views here.
