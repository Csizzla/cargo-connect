from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=50)
    Username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.Username
    
class Quote(models.Model):
    departure_city = models.CharField(max_length=50)
    delivery_city = models.CharField(max_length=50)
    weight = models.FloatField()
    dimensions =models.FloatField()
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store hashed passwords

    def __str__(self):
        return self.full_name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")  # Link to the user
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically add the timestamp
    status = models.CharField(
        max_length=50,
        choices=[
            ('Pending', 'Pending'),
            ('Processing', 'Processing'),
            ('Completed', 'Completed'),
        ],
        default='Pending',
    )
    description = models.TextField()  # Description of the order

    def __str__(self):
        return f"Order #{self.id} - {self.customer.email}"
