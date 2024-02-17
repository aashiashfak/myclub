from django.db import models
from .signal import new_instance_signal
# Create your models here.

class Products(models.Model):
    product_id = models.AutoField
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to='static/images')
    
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        is_new_instance = not self.pk
        super().save(*args, **kwargs)
        
        if is_new_instance:
            new_instance_signal.send(sender=self.__class__, instance=self, hai='hello')



