
from django.contrib import admin
from django.urls import path
from comercio.views import index
from login.views import LoginUser, RegisterUser, SalirUser
from usuario.views import ProfileDetailView , rate_profile,comment_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    #index
    path('', index, name="index"),
    #Usuario
    path('login/', LoginUser, name="login"),
    path('register/', RegisterUser, name="register"),
    path('salir/', SalirUser, name="salir"),
    path('<slug:slug>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('<slug:slug>/rate/<int:rating_value>/', rate_profile ,name='rate-profile'),
    path('<slug:slug>/comment/', comment_profile, name='comment-profile'),

    #post
]
