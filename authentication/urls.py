from django.urls import path
from authentication.views import login_view, logout_view, register_view, general_user_register_view

urlpatterns = [
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('register', register_view, name="register"),
    path('general_user_register', general_user_register_view, name='general_user_register')
]