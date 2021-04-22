from django.urls import path

from . import views

urlpatterns = [
    # Default route e.g. /
    path('', views.index, name='Index'),
    # Cart route e.g. /cart
    path('Cart', views.cart, name='Cart'),
    # Login route e.g. /login
    path('Login', views.login, name='Login'),
    # Logout route e.g. /logout
    path('Logout', views.logout, name='Logout'),
    # Login action, should never be visited directly
    path('PerformLogin', views.perform_login, name='PerformLogin'),
    # Updates the count of the cart item
    path('AdjustCartItemQuantity/<int:item_id>', views.adjust_cart_item_quantity, name='AdjustCartItemQuantity')
]