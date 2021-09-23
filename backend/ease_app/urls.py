from django.urls import path
from . import views

urlpatterns = [

    path('food/',   views.FoodList.as_view(),   name='food_list'),
    path('food/<int:pk>', views.FoodDetail.as_view(), name='food_detail'),

    path('quote/',   views.QuoteList.as_view(),   name='quote_list'),
    path('quote/<int:pk>',   views.QuoteDetail.as_view(),   name='quote_list'),
    
    path('meditate/',   views.MeditateList.as_view(),   name='meditate_list'),
    path('mediate/<int:pk>', views.MeditateDetail.as_view(), name='meditate_detail'),

]