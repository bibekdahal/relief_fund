from django.contrib import admin
from mainapp.models import ItemType, Item, Fund, Place, Provider


class ItemInline(admin.StackedInline):
    model = Item
    extra = 3

class FundAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

admin.site.register(ItemType)
admin.site.register(Fund, FundAdmin)
admin.site.register(Place)
admin.site.register(Provider)
