from django.db import models


class Customer(models.Model):
    telephone_number = models.CharField(max_length=12, primary_key=True)
    address = models.CharField(max_length=30)