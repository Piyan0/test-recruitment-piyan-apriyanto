from django.urls import path
from . import views
urlpatterns = [
  path("", views.index),
  path("product-delete", views.delete_product),
  path("product-manage?product-id=<int:product_id>", views.product_management, name="manage"),
  ]