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

class Product(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    # price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/', null=True)
    thoughness = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name



class Carusel(models.Model):
    image = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=100, null=True, blank=True)


class MenuCategories(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    explicit_url = models.CharField(max_length=100, blank=True, null=True, unique=True)
 
    def __str__(self):
        return self.name

    def children(self):
        return self.menucategories_set.all()

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []