from django.db import models
# Create your models here.

class Products(models.Model):
    product_id = models.AutoField
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='static/images')
    

    def __str__(self) -> str:
        return self.title
