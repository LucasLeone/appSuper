# Django
from django.urls import path

# Views
from products import views


urlpatterns = [
    
    path(
        route='',
        view=views.ProductsFeed.as_view(),
        name='feed'
    ),

    path(
        route='create/',
        view=views.CreateProduct.as_view(),
        name='create'
    ),

    path(
        route='search/',
        view=views.searchProduct,
        name='search'
    )

]
