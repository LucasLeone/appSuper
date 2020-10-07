# Django
from django.urls import path
from shopping_cart import views


urlpatterns = [
    
    path(
        route='',
        view=views.ListCart.as_view(),
        name='shop',
    ),

    path(
        route='add/',
        view=views.AddItem.as_view(),
        name='add'
    ),

]
