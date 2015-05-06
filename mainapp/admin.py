from django.contrib import admin
<<<<<<< HEAD
from mainapp.models import ItemType, Item, Fund, Place, Provider, AdminUser
=======
from mainapp.models import ItemType, Item, Fund, Place, Provider, BufferItem, Buffer
>>>>>>> 1d1a850bd8c1edb7e344b1c413d97d0a50b20d93


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
<<<<<<< HEAD
admin.site.register(AdminUser)
=======
admin.site.register(BufferItem)
admin.site.register(Buffer, BufferFundAdmin)
>>>>>>> 1d1a850bd8c1edb7e344b1c413d97d0a50b20d93
