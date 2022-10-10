from django.urls import path
from . import views


urlpatterns = [
    path('',views.samp,name='Home_page'),
    path('login/',views.lon,name="Login_Page"),
    path('register/',views.reg,name="Register_Page"),
    path('login/loginsub',views.loginsub),
    path('search/',views.search,name='search'),

    path('logout/',views.logout),
]