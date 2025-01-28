from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


# Create: Add a new item
def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else: 
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

# Read: List all items
def item_list(request):
    items = Item.objects.all().order_by('-created_at') # Yangi qo'shilganlar tepadan ko'rsatiladi
    return render(request, 'item_list.html', {'items': items})

# Update: Edit an existing item
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else: 
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

# Delete: Remove an item
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})
