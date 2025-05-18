from django.shortcuts import render,redirect
from . form import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import Item
# Create your views here.


def indexPage(request):
    items=Item.objects.all

    context={'items':items}
    return render(request, 'product/index.html',context)

def registerPage(request):
    
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')
        
    context={'form':form}
    
    return render(request, 'product/register.html', context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post')  # Ensure this redirect points to a valid URL name
        else:
            messages.info(request, 'Username OR Password is incorrect')
    return render(request, 'product/login.html')

def postPage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        description=request.POST.get('description')
        image=request.FILES.get('image')   

        if name and price and description:
            post=Item(name=name,price=price,description=description,image=image)
            post.save()
            return redirect('home')
    return render(request, 'product/post.html')
