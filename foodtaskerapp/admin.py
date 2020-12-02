from django.contrib import admin

# Register your models here.
from foodtaskerapp.models import Restaurant, Customer, Driver, Meal, Order, OrderDetail

class MealAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class OrderDetailAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Meal, MealAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)