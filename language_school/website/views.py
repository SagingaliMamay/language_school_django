from django.shortcuts import render


# Home page


def home(request):
    return render(request, 'home.html', {})

# About page


def about(request):
    return render(request, 'about.html', {})
