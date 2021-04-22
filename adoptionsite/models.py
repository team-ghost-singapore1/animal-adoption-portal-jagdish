from django.db import models

class CartItem(models.Model):
    """
    An item that can be placed in the cart
    """

    id = models.BigIntegerField(primary_key=True)
    quantity = models.IntegerField(default=0)
    name = models.CharField(max_length=30)

    def increment(self):
        self.quantity += 1

    def decrement(self):
        if self.quantity > 0:
            self.quantity -= 1


class Animal(models.Model):
    """
    An animal that can be adopted
    """

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    age = models.IntegerField(default=0)