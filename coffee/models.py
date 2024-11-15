from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='coffee_images/')  # Use ImageField for image uploads
    description = models.TextField(blank=True, null=True)
    origin = models.CharField(max_length=100, blank=True, null=True)
    flavor_profile = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.coffee.name} (x{self.quantity})"