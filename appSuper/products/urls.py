# Django
from django.urls import path

# Views
from products.views import views


urlpatterns = [
    
    path(
        route='',
        view=views.Feed.as_view(),
        name='feed'
    )

]
