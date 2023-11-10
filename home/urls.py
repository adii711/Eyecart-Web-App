from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # path('', views.login),
	path('', views.display, name='display'),
    
    # # path("modelform/", views.modform),
    # path("form/", views.simform),
    # path("otp/", views.otpcheck, name='user-otp'),
	# path('/home', views.home, name='home'),
	path('cart/', views.view_cart, name='view_cart'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
     path('generate_invoice/', views.generate_invoice, name='generate_invoice'),

]
