from django.db import models
# Create your models here.
class Thing(models.Model):
    CHOICES = [
        ('Essentials', 'Essentials'),
        ('Green Vegetables', 'Green Vegetables'),
        ("Today's Special", "Today's Special"),

    ]
    name=models.CharField(max_length=100)
    desc=models.TextField(max_length=1000)
    price=models.IntegerField()
    number=models.IntegerField()
    image=models.ImageField(upload_to='static/images')
    category=models.CharField(choices=CHOICES,default="Essentials",max_length=20)
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    query=models.TextField()
class Detail_item(models.Model):    # form banane ke liye home page pr
    name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    vege=models.CharField(max_length=100)
    price=models.IntegerField()
class Address(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    address=models.TextField()
