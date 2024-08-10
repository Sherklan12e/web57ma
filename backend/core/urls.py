
from django.contrib import admin
from django.urls import path
from comercio.views import index
from login.views import LoginUser, RegisterUser, SalirUser
urlpatterns = [
    path('admin/', admin.site.urls),
    #index
    path('', index, name="index"),
    #Usuario
    path('login/', LoginUser, name="login"),
    path('register/', RegisterUser, name="register"),
    path('salir/', SalirUser, name="salir"),


    #post
]
