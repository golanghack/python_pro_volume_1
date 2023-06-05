from django.shortcuts import redirect, render
from lists.models import Item

def home(request):
    
    return render(request, 'home.html')

def view_list(request):
    """View of list"""

    items = Item.objects.all()
    return render(request, 'list.html', {
        'items': items,
    })

def new_list(request):
    """-> new list""" 

    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/one/')