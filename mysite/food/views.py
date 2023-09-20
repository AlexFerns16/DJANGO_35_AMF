from django.shortcuts import render, redirect
from django.http import HttpResponse
from food.models import Item
from food.forms import ItemForm

# Create your views here.

def index(request):
    itemlist = Item.objects.all()

    context = {
        'itemlist':itemlist
    }

    return render(request, 'food/index.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)

    context = {
        'item':item
    }

    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form':form
    }

    return render(request, 'food/item-form.html', context)

def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    context = {
        'form':form
    }

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', context)
