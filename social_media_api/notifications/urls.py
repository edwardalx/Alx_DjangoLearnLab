from rest_framework.urls import path
from .views import NotificationListView

urlpatterns = [
    path('notification/', view=NotificationListView.as_view(),name='user-notifications' )
]