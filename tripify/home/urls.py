from django.urls import path
from . import views


urlpatterns = [
    path('',views.samp),
    path('login/',views.lon,name="Login_Page"),
    path('register/',views.reg,name="Register_Page"),
    path('login/loginsub',views.loginsub),
]