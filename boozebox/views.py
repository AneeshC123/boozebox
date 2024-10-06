from django.shortcuts import render, redirect, get_object_or_404
from boozebox.forms import SignUpForm, LoginForm, User
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
         
            
            user.save()
            
            return redirect('show')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def show(request):
    form=User.objects.all()
    return render(request, "show.html", {'form':form})


def edit(request, id):
    form = get_object_or_404(User, id=id)
    return render(request,'edit.html',{'form':form})

def update(request, id):
    client_details=get_object_or_404(User, id=id)
    form = SignUpForm(request.POST, instance=client_details)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html',{'form':client_details})
    

def destroy(request, id):  
    form = get_object_or_404(User, id=id)
    form.delete()  
    return redirect("/show") 

def cart(request):
    return render(request, 'cart.html')

