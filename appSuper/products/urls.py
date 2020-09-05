# Django
from django.urls import path

# Views
from products import views


urlpatterns = [
    
    path(
        route='',
        view=views.ProductsFeed.as_view(),
        name='feed'
    )

]
