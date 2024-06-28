from django.contrib import admin
from catalog.models import *
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...    

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     ...   

@admin.register(Carusel)
class CaruselAdmin(admin.ModelAdmin):
    ...    


@admin.register(MenuCategories)
class MenuCategoriesAdmin(admin.ModelAdmin):
    ...
