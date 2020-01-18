from django.shortcuts import render, redirect
from .forms import SignUpForm, LocationChoiceField
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    form = LocationChoiceField()
    if request.method == 'POST':
        form = LocationChoiceField(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index.html', {'form':form})

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

