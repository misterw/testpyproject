from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def profile_page(request):
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)