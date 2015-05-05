from django.contrib import admin
from mainapp.models import FundType, FundState, Fund, Place, Provider

admin.site.register(FundType)
admin.site.register(FundState)
admin.site.register(Fund)
admin.site.register(Place)
admin.site.register(Provider)
