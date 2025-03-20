from django.contrib.auth.views import LoginView, LogoutView
from .views import Home, Register,Profile,Post, ListView, DetailView,CreateView,UpdateView,DeleteView,CommentCreateView,CommentListView,CommentUpdateView,CommentDeleteView,CommentDetailView 
from django.urls import path, include

urlpatterns = [
    path('', view=Home.as_view(), name='home'),
    path('login/', view=LoginView.as_view(template_name = "/blog/login.html"), name='login'), 
    path('logout/', view=LogoutView.as_view(template_name = "/blog/logout.html"), name='logout'),
    path('register/', view=Register.as_view(), name='register'),
    path('profile/', view=Profile.as_view(), name='profile' ),
    path('post/', view= Post.as_view(), name = 'posts'),
    path('posts/', view= ListView.as_view(), name = 'list-posts'),
    path('post/<int:pk>/', view= DetailView.as_view(), name = 'detail-posts'),
    path('post/new/', view= CreateView.as_view(), name = 'create-posts'),
    path('post/<int:pk>/update/', view= UpdateView.as_view(), name = 'update-posts'),
    path('post/<int:pk>/delete/', view= DeleteView.as_view(), name = 'delete-posts'),
    path('post/<int:pk>/comments/new/',view= CommentCreateView.as_view(), name='create_comment'),
    path('post/<int:pk>/comments/',view= CommentListView.as_view(), name='list_comments'),
    path('post/<int:pk>/comments/<int:pk>/',view= CommentDetailView.as_view(), name='comment'),
    path('comment/<int:pk>/update/',view= CommentUpdateView.as_view(), name='update_comments'),
    path('comment/<int:pk>/delete/',view= CommentDeleteView.as_view(), name='delete_comments'),

]



#["comment/<int:pk>/update/", "post/<int:pk>/comments/new/", "comment/<int:pk>/delete/"]