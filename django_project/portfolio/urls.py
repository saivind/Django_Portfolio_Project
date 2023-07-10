from django.conf import settings
from django.urls import path
from portfolio.views import api_np

app_name='portfolio'

urlpatterns = [
                              path('info', api_np, name='info_NP'),
]
