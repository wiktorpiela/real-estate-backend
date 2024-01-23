from django.urls import path
from . import views

urlpatterns = [
    path('listing-list/', views.ListingList.as_view(), name="listingList"),
    path('listing-create/', views.ListingCreate.as_view(), name="listingCreate"),
]