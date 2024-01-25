from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('profile-list/', views.ProfileList.as_view(), name="profileList"),
    path('profile-details/<int:seller>', views.ProfileDetails.as_view(), name="profileDetails"),
    path('profile-update/<int:seller>', views.ProfileUpdate.as_view(), name="profileUpdate"),
]