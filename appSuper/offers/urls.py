# Django
from django.urls import path

# Views
from offers import views


urlpatterns = [
    path(
        route='',
        view=views.OffersFeed,
        name='offers'
    )
]
