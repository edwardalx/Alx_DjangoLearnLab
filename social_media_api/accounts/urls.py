from django.urls import path,include
from .views import CustomUserRegisterApi, CustomUserLoginAPIView,ProfileManagementView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile',ProfileManagementView)
urlpatterns=[
   path('api/register', view=CustomUserRegisterApi.as_view(),name='register-api' ),
   path('api/login', view=CustomUserLoginAPIView.as_view(), name='login-api'),
   path('', include(router.urls)),

]