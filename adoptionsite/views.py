from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse
import pandas

from adoptionsite.models import CartItem, Animal

login_ids = [ 'pencil', 'flower', 'icecream', 'basketball', 'orange', 'placeholder' ]

# Initial load of animals
available_animals = []
animals_df = pandas.read_csv('animals.csv', index_col='Id')

for animal in animals_df.itertuples():
    available_animals.append(Animal(id=animal.Index, name=animal.Name, description=animal.Description, age=animal.Age))

cart_items = [
    CartItem(id=0, quantity=0, name=available_animals[0].name),
    CartItem(id=1, quantity=0, name=available_animals[1].name),
    CartItem(id=2, quantity=0, name=available_animals[2].name),
    CartItem(id=3, quantity=0, name=available_animals[3].name)
]


def index(request):
    context = {
        'available_animals': available_animals
    }

    return render(request, 'adoptionsite/index.html', context)

def cart(request):
    context = {
        'cart_items': cart_items
    }

    return render(request, 'adoptionsite/cart.html', context)

def login(request):
    context = {
        'login_ids': login_ids
    }

    return render(request, 'adoptionsite/login.html', context)

def logout(request):
    return render(request, 'adoptionsite/logout.html')

def perform_login(request):
    provided_username = request.POST['AvatarId']
    provided_password = request.POST.get('password')

    user = authenticate(request, username=provided_username, password=provided_password)

    if user is not None:
        auth_login(request, user)

        return redirect('Index')
    else:
        context = {
            'login_ids': login_ids,
            'error_message': 'Invalid username or password.'
        }

        return render(request, 'adoptionsite/login.html', context)

def adjust_cart_item_quantity(request, item_id):
    cart_item = next((item for item in cart_items if item.id == item_id))
    action = request.POST['action']

    if action == "increment":
        cart_item.increment()
    else:
        cart_item.decrement()

    return redirect('Cart')
