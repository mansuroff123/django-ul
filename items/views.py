from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.

def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else: 
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})


def item_list(request):
    items = Item.objects.all().order_by('-created_at') # Yangi qo'shilganlar tepadan ko'rsatiladi
    return render(request, 'item_list.html', {'items': items})

