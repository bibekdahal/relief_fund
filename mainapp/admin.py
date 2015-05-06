from django.contrib import admin
from mainapp.models import ItemType, Item, Fund, Place, Provider, BufferItem, Buffer


class ItemInline(admin.StackedInline):
    model = Item
    extra = 3

class FundAdmin(admin.ModelAdmin):
    inlines = [ItemInline]

class BufferItemInline(admin.StackedInline):
    model = BufferItem
    extra = 3

class BufferFundAdmin(admin.ModelAdmin):
    inlines = [BufferItemInline]

admin.site.register(ItemType)
admin.site.register(Item)
admin.site.register(Fund, FundAdmin)
admin.site.register(Place)
admin.site.register(Provider)
admin.site.register(BufferItem)
admin.site.register(Buffer, BufferFundAdmin)
