from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import PostViewSet, CommentViewSet,PostFeedView, like_post
router = DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comment',CommentViewSet )

urlpatterns=[

   path('', include(router.urls)),
   path('feed/', view=PostFeedView.as_view, name='post-feed'),
   path('posts/<int:id>/like/', view=like_post, name='like-post'),
]