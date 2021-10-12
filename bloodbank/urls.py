from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('bld/',views.add_donor,name='bld'),
    path('display/',views.display,name='display'),
    path('signuup/',views.signuup,name='signuup'),
    # path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')


]
    