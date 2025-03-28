from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import PostViewSet, CommentViewSet
router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comment',CommentViewSet )

urlpatterns=[

   path('', include(router.urls)),
   
   
]