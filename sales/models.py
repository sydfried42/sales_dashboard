from django.db import models


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True) 
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.IntegerField(unique=True)
    customer_id = models.IntegerField()
    status = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f"Order {self.order_id} by Customer {self.customer_id}"

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Payment for Order {self.order.order_id} - {self.payment_method}"
