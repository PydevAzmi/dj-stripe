from django.urls import path ,include
from .views import (CreateCheckoutSession, 
                    Home
                    )
app_name = "payment"

urlpatterns = [
    path("", Home.as_view(), name= "home"),
    path("pay", CreateCheckoutSession.as_view(), name= "checkout"),
]
