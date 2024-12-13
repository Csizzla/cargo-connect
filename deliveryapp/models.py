from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Member(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store hashed passwords

    def __str__(self):
        return self.full_name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name



class Order(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="order", null=True, blank=True)  # Link to the Quote
    departure_city = models.CharField(max_length=100)
    delivery_city = models.CharField(max_length=100)
    weight = models.FloatField()
    dimensions = models.CharField(max_length=100)
    driver = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[("Pending", "Pending"),("in transit","in transit"), ("Completed", "Completed"), ("Canceled", "Canceled")],
        default="Pending",
    )

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Feedback(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def get_active_orders(member):
    return Order.objects.filter(member=member, status="Pending")

def get_completed_orders(member):
    return Order.objects.filter(member=member, status="Completed")