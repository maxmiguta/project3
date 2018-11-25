# The 'register' view here handles taking a new user's email and password and creates their account

from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "Unable to log you in at this time")

    else:
        form = UserRegistrationForm()

    args = {'form': form}

    return render(request, 'register.html', args)


# The '@login_required' decorator is used to restrict access
@login_required(login_url='/login/')
def profile(request):
    """A view that displays the profile page of a logged in user"""
    return render(request, 'profile.html')


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                form.add_error(None, "Your username or password are incorrect")
    else:
        form = UserLoginForm()

    args = {'form': form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required()
def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))