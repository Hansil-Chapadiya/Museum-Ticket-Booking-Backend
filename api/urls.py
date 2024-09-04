from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('pyadmin/museums/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('pyadmin/museums/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('pyadmin/museums/getMuseums/', views.getMuseums),
    path('pyadmin/museums/getMuseum/<str:id>/', views.getMuseum),
    path('pyadmin/museums/addMuseum/', views.addMuseum),
    path('pyadmin/museums/updateMuseum/<str:id>/', views.updateMuseum)
]
