# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    # Agregar clases al formulario
    form.fields['username'].widget.attrs.update({'class': 'form-control'})
    form.fields['password1'].widget.attrs.update({'class': 'form-control'})
    form.fields['password2'].widget.attrs.update({'class': 'form-control'})
    
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        
    # Agregar clases al formulario
    form.fields['username'].widget.attrs.update({'class': 'form-control'})
    form.fields['password'].widget.attrs.update({'class': 'form-control'})
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
