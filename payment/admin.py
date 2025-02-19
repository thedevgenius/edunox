from django.contrib import admin
from .models import FeesType, Fees
# Register your models here.
admin.site.register(FeesType)
# admin.site.register(Fees)

class FeesAdmin(admin.ModelAdmin):
    list_display = ('type', 'grade', 'amount', 'is_monthly', 'status')

admin.site.register(Fees, FeesAdmin)

