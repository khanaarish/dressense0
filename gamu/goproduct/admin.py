from django.contrib import admin

# Register your models here.


from .models import Go_category, Go_product

admin.site.register(Go_category)
admin.site.register(Go_product)
