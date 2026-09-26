from django.db import models
from django.contrib.auth.models import User


class Trip(models.Model):
    TRIP_STATUS = (
        ('planned', 'Planned'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip_name = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=TRIP_STATUS, default='planned')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trip_name


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('transport', 'Transport'),
        ('food', 'Food'),
        ('hotel', 'Hotel'),
        ('shopping', 'Shopping'),
        ('entertainment', 'Entertainment'),
        ('misc', 'Miscellaneous'),
    )

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    PAYMENT_METHODS = (
        ('cash', 'Cash'),
        ('upi', 'UPI'),
        ('card', 'Card'),
        ('wallet', 'Wallet'),
    )

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='expenses')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    expense_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    receipt = models.ImageField(upload_to='receipts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trip.trip_name} - ₹{self.amount}"


class TravelCompanion(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='companions')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class ExpenseSplit(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    companion = models.ForeignKey(TravelCompanion, on_delete=models.CASCADE)
    share_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.companion.name} - ₹{self.share_amount}"