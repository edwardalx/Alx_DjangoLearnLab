from django.urls import path,include
from .views import CustomUserRegisterApi, CustomUserLoginAPIView,ProfileManagementView,follow_user,unfollow_user
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile',ProfileManagementView)
urlpatterns=[
   path('register/', view=CustomUserRegisterApi.as_view(),name='register-api' ),
   path('login/', view=CustomUserLoginAPIView.as_view(), name='login-api'),
   path('', include(router.urls)),
   path('follow/<int:user_id>',view=follow_user , name='folloe-user'),
   path('unfollow/<int:user_id>/', view=unfollow_user, name='Unfollow-user'), 
  
]