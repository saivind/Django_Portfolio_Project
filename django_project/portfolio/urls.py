from django.conf import settings
from django.urls import path



from . import views

app_name='portfolio'

urlpatterns = [
#NP_API
                              path('results',views.api_np, name='results'),
                              path('info_NP',views.api_np, name='info_NP'),
]
