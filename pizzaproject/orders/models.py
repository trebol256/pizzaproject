from django.db import models



PIZZA_TYPES = (('Margherita', 'Margherita'), 
                ('Pepperoni', 'Pepperoni'), 
                ('Vegetarian', 'Vegetarian'),)
class Orderrequest(models.Model):
    pizzatype = models.CharField(max_length=100, choices=PIZZA_TYPES)
    commentorder = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pizzatype} - {self.commentorder}"

    