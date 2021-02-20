"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Virgis Plants',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact Virgis Plants',
            'message':'We are happy to speak to you and help you decide which plants are best for you',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About Virgis Plants',
            'message':'The plants Virginia breeds are bred to add a natural touch to your home, and help you relieve stress',
            'year':datetime.now().year,
        }
    )

def plants(request):
    """Renders the plants page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/plants.html',
        {
            'title':'Our Plants',
            'message':'Learn More About The Plants We Carry',
            'year':datetime.now().year,
        }
    )

def gallery(request):
    """Renders the gallery page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/gallery.html',
        {
            'title':'Plant Gallery',
            'message':'See The Beautiful Plants We Carry',
            'year':datetime.now().year,
        }
    )

def buy(request):
    """Renders the how to buy page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/buy.html',
        {
            'title': 'Interested In Buying Virgis Plants',
            'message': 'You Can Buy Our Plants Throught Different Online Stores and Websites',
            'year': datetime.now().year,
        }
    )