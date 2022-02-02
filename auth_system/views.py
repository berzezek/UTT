from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate



def logoutuser(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')

def loginuser(request):
    form = AuthenticationForm()
    if request.method == 'GET':
        return render(request, 'auth_system/loginuser.html', {'form': form})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'auth_system/loginuser.html', {'form': form, 'error': 'User or password did not match'})
        else:
            login(request, user)
            return redirect('home')
