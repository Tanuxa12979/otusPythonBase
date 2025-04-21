from django.contrib import admin
from .models import Product, Category

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', "created_at")
    list_filter = ('name', 'price')
    search_fields = ('name', 'description')
    search_help_text = "Search by name or description"

    @admin.action(description="Make price 100 hire")
    def set_hire_price(self, request, queryset):
        for product in queryset:
            product.price += 100
            product.save()
        self.message_user(request, "Price now is hire")

    actions = [set_hire_price]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)
    search_help_text = "Search by name"


