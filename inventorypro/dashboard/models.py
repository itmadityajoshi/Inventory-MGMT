from django.db import models

# Create your models here.


CATEGORY = (
    ('stationaries','stationaries'),
    ('Food','Food'),
    ('Electronics','Electronics'),
    ('Household','Household'),
  )

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()