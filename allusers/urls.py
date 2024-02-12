from django.urls import path
from account.views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign-up/', register, name='sign-up')
]
