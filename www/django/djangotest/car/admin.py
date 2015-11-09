from django.contrib import admin
from car.models import Car, Make

class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','make','locality')
    search_fields = ['name']

class MakeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Car, CarAdmin)
admin.site.register(Make, MakeAdmin)

