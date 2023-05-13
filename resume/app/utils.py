def change_theme(th, url):
    params = {'svg': 'light', 'change': 'Light Mode', 'link': f'{url}?theme=light'}
    if th is not None:
        if th == 'light':
            params = {'svg': 'dark', 'change': 'Dark Mode', 'link': f'{url}?theme=dark'}
    return params