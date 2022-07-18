from django.shortcuts import render


# All functions for all pages


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def course_details(request):
    return render(request, 'course_details.html', {})


def courses(request):
    return render(request, 'courses.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def events(request):
    return render(request, 'events.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def trainers(request):
    return render(request, 'trainers.html', {})
