from django.urls import path,include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserToken

router = DefaultRouter()
router.register(r'Book', BookViewSet)

urlpatterns = [
path('book/', view=BookList.as_view(), name='book-list'),
path('', include(router.urls)),
path('user/token/', view=UserToken.as_view(), name='userApi'),
]