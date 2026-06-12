from django.db import models

# Create your models here.
class Product(models.Model):
     title = models.CharField(max_length=200)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     description = models.TextField()
     image_url = models.URLField(max_length=500, blank=True, null=True)
     stock = models.IntegerField(default=10)

     def __str__(self):
          return self.title