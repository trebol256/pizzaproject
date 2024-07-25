from django.urls import path

from . import views

app_name = "orders"
urlpatterns = [
    path("", views.order_request, name="order_request"),
    path("orders/", views.order_table, name="order_table"),
]