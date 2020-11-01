from django.shortcuts import render
# Create your views here.
from .models import Thing,Detail_item
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,SignUpForm,ContactForm,Detail_itemForm,AddressForm,ThingForm
from django.contrib import messages
from django.http import HttpResponseRedirect
def user_signup(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'You have successfully signed up')
    else:
        fm=SignUpForm()
    return render(request,'registration/signup.html',{'form':fm})
def home(request):
    if request.method=="POST":
        fm=Detail_itemForm(request.POST)
        reg=Detail_item(name=request.user,quantity=request.POST['quantity'],vege=request.POST['vege'],price=request.POST['price'])
        reg.save()
    fm=Detail_itemForm()
    obj=Thing.objects.all()
    #print(obj)
    objg=Thing.objects.filter(category="Green Vegetables")
    obje=Thing.objects.filter(category="Essentials")
    objs=Thing.objects.filter(category="Today's Special")
    #print("Essentials",obje)


    return render(request,'kisan/home.html',{'objg':objg,'obje':obje,'objs':objs,'form':fm})
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=LoginForm(request=request.POST,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/')
                else:
                    messages.error(request,"Username and Password do not match in our database.")
        else:
            fm=LoginForm()
        return render(request,'registration/login.html',{'form':fm})
    else :
        return HttpResponseRedirect('/')
def user_logout(request):
    logout(request)
    obj=Thing.objects.all()
    objg = Thing.objects.filter(category="Green Vegetables")
    obje = Thing.objects.filter(category="Essentials")
    objs = Thing.objects.filter(category="Today's Special")
    return HttpResponseRedirect('/')
def contact(request):
    if request.method=="POST":
        fm=ContactForm(request.POST)
        fm.save()
        messages.success(request,"We will answer you as soon as possible.")
    else :
        fm=ContactForm()
    return render(request,'kisan/contact.html',{'form':fm})
def cart(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=AddressForm(request.POST)
            if fm.is_valid():
                fm.save()
                return render(request,'kisan/place.html')
        else:
            fm=AddressForm()
        obj=Detail_item.objects.filter(name=request.user)
        return render(request,'kisan/cart.html',{'form':fm,'obj':obj})
    else :
        messages.error(request,"You must login first.")
        return HttpResponseRedirect('/login')
def sell(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm=ThingForm(request.POST,request.FILES)
            print(request.FILES)
            if fm.is_valid():
                fm.save()
                messages.success(request," You have successfully added your product for selling. ")
        else:
            fm=ThingForm()
        return render(request,'kisan/sell.html',{'form':fm})
    else:
        messages.error(request,'You must login first')
        return HttpResponseRedirect('/login')
def place(request):
    if request.user.is_authenticated:

        return render(request,'kisan/place.html')
    else :
        messages.error(request,"You must login first.")
        return HttpResponseRedirect('/login')
        #return render(request,'registration/login.html')
def search(request):

    return render(request,'kisan/search.html')