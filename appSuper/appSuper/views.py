# Django
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class Map(TemplateView):
    template_name = 'map.html'