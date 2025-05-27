from django.urls import path
from recipes.views import home, sobre, contato



urlpatterns = [
    path('sobre/', sobre),
    path('', home),
    path('contato/', contato)
]