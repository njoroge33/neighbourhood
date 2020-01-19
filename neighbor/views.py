from django.shortcuts import render, redirect
from .forms import SignUpForm, ProfileForm, BusinessForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    current_user = request.user
    
    return render(request, 'index.html', {'current_user':current_user})

def signup(request):
    name = 'Signup'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'name':name})


def profile(request):
    current_user = request.user
    
    return render(request, 'profile.html', {'current_user':current_user,})

def update_profile(request):
    current_user = request.user
    profile = Profile(user=request.user)
   
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,  instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user= current_user
            profile.save()
        return redirect('home')
    else:
        form = ProfileForm(instance=request.user.profile)
        args = {}
        args.update(csrf(request))
        args['form'] = form
    return render(request, 'update_profile.html', {'current_user':current_user, 'form':form})

def new_business(request):
    current_user = request.user

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user= current_user
            business.save()
        return redirect('home')
    else:
        form = BusinessForm()
    return render(request, 'business.html', {'current_user':current_user, 'form':form})
