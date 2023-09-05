from currency.models import Currency
from currency.scraper import current_currency_rate

from rest_framework.views import APIView
from rest_framework.response import Response
import multiprocessing


class GetCurrencyData(APIView):
    def get(self, request, *args, **kwargs):
        currency_queryset = Currency.objects.filter(is_allowed=True)
        currency_list = list(currency_queryset.values_list('name', flat=True))
        currency_persian_list = list(currency_queryset.values_list('persian_name', flat=True))

        pool = multiprocessing.Pool(processes=len(currency_list))
        currency_data = pool.map(current_currency_rate, currency_list)

        pool.close()
        pool.join()

        prices = []
        changes = []

        for data in currency_data:
            parts = data.split()
            if len(parts) == 2:
                price, change = parts
                formatted_price = '{:,}'.format(int(price.replace(',', '')))
                prices.append(formatted_price)
                changes.append(change)
            else:
                prices.append(None)
                changes.append(None)

        currency_data_list = [
            {'id': str(i + 1), 'name': name, 'persian_name': persian_name, 'price': price or "-",
             'changes': change or "-",
             'status': 'pos' if change and (
                     change[0] == '+' or not any(char in change for char in '+-')) else 'neg' if change and change[
                 0] == '-' else None}
            for i, (name, persian_name, price, change) in
            enumerate(zip(currency_list, currency_persian_list, prices, changes))]

        return Response(data=currency_data_list)
