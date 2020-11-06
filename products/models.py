from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
import datetime as dt
from users.models import Profile

class Product(models.Model):
    """
    Product class to define Product attributes
    """
    tags= (
        ('Men', 'Men'),
        ('Ladies', 'Ladies'),
        ('Kids', 'Kids'),
    )
    name = models.CharField(max_length =200)
    product_image = ImageField(blank=True, manual_crop="")
    description = models.CharField(max_length =300)
    category = models.CharField(choices=tags,max_length =100,default='')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 


class Product_Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment      