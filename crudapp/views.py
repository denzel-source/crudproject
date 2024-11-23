from django.shortcuts import render, redirect

from .models import Item
# Create your views here.
# CRUD

# Create
def create_item(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Item.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request,'item_form.html')

# Read
def item_list(request):
    items = Item.objects.all()
    return render(request,'item_list.html',{'items':items})

# Update
def update_item(request,pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.save()
        return redirect('item_list')
    return render(request,'item_form.html',{'item':item})

# Delete
def delete_item(request,pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request,'item_confirm_delete.html',{'item':item})