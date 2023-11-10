"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
	path('index/', views.display, name='display'),
    
    # path("modelform/", views.modform),
    path("form/", views.simform),
    path("otp/", views.otpcheck,name="otp"),
	# path('/home', views.home, name='home'),
	path('cart/', views.view_cart, name='view_cart'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
     path('generate_invoice/', views.generate_invoice, name='generate_invoice'),

    # Update the quantity of items in the cart
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
