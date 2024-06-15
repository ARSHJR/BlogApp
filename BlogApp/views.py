from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def header(request):
    return render(request, "header.html")

def login(request):
    return render(request, "loginPage.html")

def register(request):
    return render(request, "register.html")