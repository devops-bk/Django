from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        db_table = 'Users'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return "{} ({})".format(self.name, self.price)

    class Meta:
        db_table = 'Products'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return "Order Id : {}".format(self.id)

    class Meta:
        db_table = 'Orders'