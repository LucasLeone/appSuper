# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Views
from appSuper import views

urlpatterns = [

    path('admin/', admin.site.urls),

    #   Apps
    path('products/', include(('products.urls', 'products'), namespace='products')),
    # path('shopping_cart/', include(('shopping_cart.urls', 'shopping_cart'), namespace='shopping_cart')),

    #   Local
    path(
        route='',
        view=views.Home.as_view(),
        name='home'
    ),

    path(
        route='map/',
        view=views.Map.as_view(),
        name='map'
    )

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
