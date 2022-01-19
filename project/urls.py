from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from django.conf.urls.static import static
from django.conf import settings

from project import views

urlpatterns = [
    path('login/', obtain_auth_token),
    path('register/', views.UserRegister.as_view()),
    path('cars/', views.CarView.as_view()),
    path('car/update/', views.CarUpdate.as_view()),
    path('car/delete/', views.CarDelete.as_view()),
    path('users/', views.AppUserView.as_view()),
    path('cities/', views.CityView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)