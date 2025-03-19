from django.contrib.auth.views import LoginView, LogoutView
from .views import Home, Register
from django.urls import path, include

urlpatterns = [
    path('', view=Home.as_view(), name='home'),
    path('login/', view=LoginView.as_view(template_name = "/blog/login.html"), name='login'), 
    path('logout/', view=LogoutView.as_view(template_name = "/blog/logout.html"), name='logout'),
]