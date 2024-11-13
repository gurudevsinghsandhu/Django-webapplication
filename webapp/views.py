# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from .forms import UserRegistrationForm, UserLoginForm

# def signup(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account created successfully!')
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'webapp/signup.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid credentials')
#     else:
#         form = UserLoginForm()
#     return render(request, 'webapp/login.html', {'form': form})

# @login_required
# def user_logout(request):
#     logout(request)
#     messages.success(request, 'You have been logged out.')
#     return redirect('login')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, 'webapp/home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('/login/')
            except:
                messages.error(request, 'Username already exists!')
        else:
            messages.error(request, 'Passwords do not match!')
    
    return render(request, 'webapp/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('base')
        else:
            messages.error(request, 'Invalid credentials')
    
    return render(request, 'webapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def base_view(request):
  return render(request, 'webapp/base.html')

