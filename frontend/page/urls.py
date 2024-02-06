from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


class CustomLogoutView(LogoutView):
    next_page = '/logged_out/'


urlpatterns = [
    path('', index, name="index"),
    path('index/', login_view, name='login_view'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('<str:pagename>/', index, name='index'),
    path('student/register/', student_register, name="register"),
]
