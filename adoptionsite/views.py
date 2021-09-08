import pandas
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from adoptionsite.models import Animal, CartItem

login_ids = [ 'pencil', 'flower', 'icecream', 'basketball', 'orange', 'placeholder' ]

# Initial load of animals
available_animals = []

# Load animals from CSV
animals_df = pandas.read_csv('animals.csv', index_col='Id')

for animal in animals_df.itertuples():
    available_animals.append(Animal(id=animal.Index, name=animal.Name, description=animal.Description, age=animal.Age))

# # Uncomment this and fill in the details to load the animals from Mongo DB
# # Don't forget to remove the code above that is no longer required and the pandas
# # package can also be removed from the requirements.txt file
# mongo_db_uri = 'mongodb://<resource-name>:<primary-password>@<host>:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@<resource-name>@'
# mongo_client = pymongo.MongoClient(mongo_db_uri)

# # This is your database name (TAA_Portal)
# mongo_db = mongo_client.TAA_Portal

# # This is your collection name (AvailableAnimals)
# mongodb_animals = mongo_db.AvailableAnimals

# for animal in mongodb_animals.find():
#     available_animals.append(Animal(id=animal['id'], name=animal['name'], description=animal['description'], age=animal['age']))


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
