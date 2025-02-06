# yourapp/urls.py
from django.urls import path
from .views import work_with_us

urlpatterns = [
    path('', work_with_us, name='work_with_us'),
]
