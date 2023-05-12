from django.shortcuts import render, redirect

# Create your views here.
def show_cv(r):
    theme = r.GET.get('theme')
    current_url = r.path
    params = {'svg': 'light', 'change': 'Light Mode', 'link': f'{current_url}?theme=light'}
    if theme is not None:
        if theme == 'light':
            params = {'svg': 'dark', 'change': 'Dark Mode', 'link': f'{current_url}?theme=dark'}
    data = {'params': params}
    return render(r, 'index.html', data)

def index(r):
    return redirect('/resume/show/')