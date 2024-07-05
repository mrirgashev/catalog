from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=100)
    cat_image = models.ImageField(upload_to='media/',null=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media/', null=True)
    thoughness = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name



class Carusel(models.Model):
    image = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=100, null=True, blank=True)

