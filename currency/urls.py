from django.urls import path
from .views import GetCurrencyData

app_name = "currency"

urlpatterns = [
    path("", GetCurrencyData.as_view(), name="get_currency_data"),
]
