from django.contrib import admin
from currency.models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("name", "persian_name", "is_allowed")
    list_editable = ("persian_name", "is_allowed",)
