from django.db import models

# Create your models here.


CATEGORY = (
    ('stationaries','stationaries'),
    ('Food','Food'),
    ('Electronics','Electronics'),
    ('Household','Household'),
  )

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)


    def __str__(self):
        return f"{self.name} - {self.quantity}"
    