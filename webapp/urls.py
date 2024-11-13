# from django.urls import path
# from webapp.views import *

# urlpatterns=[
#     path('signup/',signup,name='signup'),
#     path('login/',login,name='login'),
#     path('home/',home,name='home'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('base/', views.base_view, name='base'),
]
