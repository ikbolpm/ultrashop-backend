from django.urls import path

from .views import DollarExchangeRateListView

urlpatterns = [
    path('', DollarExchangeRateListView.as_view(), name='dollar-rate'),
]
