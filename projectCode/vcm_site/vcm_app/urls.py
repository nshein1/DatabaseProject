from django.urls import path

from . import views

urlpatterns = [

    # ex: /vcm/
    path('', views.index, name='index'),


    # ex: /vcm/vendors/
    path('vendors/', views.vendors, name='vendors'),

    #ex /vcm/vendors/1/
    path('vendors/<int:vendor_id>/', views.vendor_detail, name='vendor detail'),

    # ex: /vcm/contracts/
    path('contracts/', views.contracts, name='contracts'),

     #ex /vcm/contracts/1/
    path('contracts/<int:contract_id>/', views.contract_detail, name='contract detail'),
]