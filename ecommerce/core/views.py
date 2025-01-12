from django.shortcuts import render
from django.http import HttpResponse

from item.models import Catagory, Item


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    catagories = Catagory.objects.all()
    return render(request, 'core/index.html',
                  {'items': items, 'catagories': catagories})


def contact(request):
    return render(request, 'core/contact.html')
