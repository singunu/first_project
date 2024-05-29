from django.urls import path
from . import views

urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products),
    path('deposit-products/', views.deposit_products),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options),
    path('save-saving-products/', views.save_saving_products),
    path('saving-products/', views.saving_products),
    path('saving-product-options/<str:fin_prdt_cd>/', views.saving_product_options),
    path('update-deposit-products/', views.update_deposit_products, name='update_deposit_products'),
    path('update-saving-products/', views.update_saving_products, name='update_saving_products'),
    path('filtered-deposit-products/', views.filtered_deposit_products, name='filtered_deposit_products'),
    path('filtered-saving-products/', views.filtered_saving_products, name='filtered_saving_products'),
    path('top-deposit-products/', views.top_deposit_products, name='top_deposit_products'),
    path('top-saving-products/', views.top_saving_products, name='top_saving_products'),
    path('favorite/deposit/add/', views.add_favorite_deposit_product, name='add_favorite_deposit_product'),
    path('favorite/deposit/', views.list_favorite_deposit_products, name='list_favorite_deposit_products'),
    path('favorite/deposit/remove/<int:product_id>/', views.remove_favorite_deposit_product, name='remove_favorite_deposit_product'),
    path('favorite/saving/add/', views.add_favorite_saving_product, name='add_favorite_saving_product'),
    path('favorite/saving/', views.list_favorite_saving_products, name='list_favorite_saving_products'),
    path('favorite/saving/remove/<int:product_id>/', views.remove_favorite_saving_product, name='remove_favorite_saving_product'),
]