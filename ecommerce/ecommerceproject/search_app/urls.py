from django.urls import path
from . import views


app_name='search_app'
urlpatterns=[
    # path('add/<int:product_id>/', views., name='add_cart'),
    path('', views.SearchResult,name='SearchResult'),

]