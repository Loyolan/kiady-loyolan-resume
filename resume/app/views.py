from django.shortcuts import render, redirect
from app import utils

# Create your views here.

def index(r):
    return redirect('/resume/show/')

def show(r):
    return redirect('/resume/show/loyolan')

def show_cv(r, user):
    theme = r.GET.get('theme')
    current_url = r.path
    title = "Kiady LoyOlan"
    params = utils.change_theme(theme, current_url)
    data = {'params': params, 'title': title}
    return render(r, 'index.html', data)