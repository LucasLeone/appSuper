# Django
from django.views.generic import ListView


class OffersFeed(ListView):
    template_name = 'offers/feed.html'
    model = Offer
    context_object_name = 'offers'