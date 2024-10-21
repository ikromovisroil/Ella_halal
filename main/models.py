from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.TextField(null=True, blank=True)
    summa = models.PositiveIntegerField()
    status = models.BooleanField(default=True)
    action = models.BooleanField(default=False)
    action_summa = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='product')
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    title = models.TextField()
    # date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'contact'
        