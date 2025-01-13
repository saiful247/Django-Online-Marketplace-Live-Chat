from django.shortcuts import render, redirect
from django.http import HttpResponse

from item.models import Catagory, Item

from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    catagories = Catagory.objects.all()
    return render(request, 'core/index.html',
                  {'items': items, 'catagories': catagories})


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {
        'form': form
    })
