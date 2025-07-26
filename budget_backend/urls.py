from django.contrib import admin
from django.urls import path
from api.views import get_transactions, add_transaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/', get_transactions),      
    path('add_transaction/', add_transaction),    
]