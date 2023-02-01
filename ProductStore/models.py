from django.db import models
from UserAuth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,blank=True)
    slug = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Artist(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    name = models.CharField(max_length=50,blank=True)
    slug = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    category_id = models.ForeignKey(category_id=Category)
    artist_id = models.ForeignKey(artist_id=Artist)
    price = models.FloatField()
    special_price = models.FloatField(null=True,blank=True,default=None)
    discount_percent = models.IntegerField(default=0)
    image_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=False)
    stock = models.IntegerField()
    is_parent = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10)
    ADDRESS_TYPE = {
        'H':'HOME',
        'W':'WORK',
        'O':'OTHER'

    }
    address_type = models.CharField(choices=ADDRESS_TYPE,max_length=1,default='H')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AddressItems(models.Model):
    address_id = models.ForeignKey(address_id=Address)
    user_id = models.ForeignKey(user_id=User)

class Order(models.Model):
    user_id = models.ForeignKey(user_id=User)
    amount = models.FloatField()
    ORDER_STATUS= {
        'PE':'PENDING',
        'RP':'READY TO PICKUP',
        'IN':''
    }
    status = models.CharField(choices=ORDER_STATUS)