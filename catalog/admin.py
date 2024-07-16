from django.contrib import admin
from catalog.models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'capacity', 'image', 'subcategory', 'category', 'thoughness', 'type', 'purpose')

    def save_model(self, request, obj, form, change):
        # Automatically set the category based on the selected subcategory
        if obj.subcategory and obj.subcategory.category:
            obj.category = obj.subcategory.category
        super().save_model(request, obj, form, change)

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product, ProductAdmin)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    ...

@admin.register(Carusel_up_to_five_images)
class Carusel_up_to_five_imagesAdmin(admin.ModelAdmin):
    ...    
    

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    ...    



