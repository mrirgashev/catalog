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
    capacity = models.IntegerField(null=True)
    image = models.ImageField(upload_to='media/', null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    thoughness = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    purpose = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name



class Carusel_up_to_five_images(models.Model):
    ''' Up to 5 images '''
    image = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=100, null=True, blank=True) 

    def __str__(self):
        return self.image.name

class New(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title