from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('about/',views.about,name='aboutpage'),
    path('login/',views.log,name='logpage'),
    path('register/',views.register,name='registerpage'),
    path('logout/',views.logout,name='logoutpage'),
    path('order/',views.order,name='orderpage')
    
]