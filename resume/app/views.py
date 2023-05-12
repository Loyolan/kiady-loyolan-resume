from django.shortcuts import render, redirect

# Create your views here.
def show_cv(r):
    
    return render(r, 'index.html')

def index(r):
    return redirect('/resume/show/')