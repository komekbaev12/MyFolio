from django.urls import path
from folio.views import index


urlpatterns = [
    path('index/', index, name='index')
]