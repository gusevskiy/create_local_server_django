from django.urls import path

from . import views


app_name = "catalogs"

urlpatterns = [
    path("", views.index, name="index"),
    path("catalog/", views.catalog, name="catalog"),
    path("catalog/<int:pk>/", views.catalog_detail, name="catalog_detail"),
]