from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.urls import reverse_lazy
from .forms import MyForm,PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from taggit.models import Tag
# Create your views here.

class Home(generic.TemplateView):
    template_name = 'blog/base.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] =  'Welcome to our site!'
        return context
class Post(generic.ListView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'


class Register(generic.CreateView):
    template_name = 'blog/register.html'
    form_class = MyForm
    success_url = reverse_lazy('login')

class Profile(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = MyForm
    template_name = 'blog/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = MyForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = MyForm(instance = user)

    context = {'form':form}
    return render(request, 'profile.html', context)
            
""" Another way of doing this by inheriting view
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect
from .forms import MyForm

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(View):
    def get(self, request):
        form = MyForm(instance=request.user)
        return render(request, 'profile.html', {'form': form})

    def post(self, request):
        form = MyForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'profile.html', {'form': form})"""

class ListView(generic.ListView):
    template_name = 'blog/post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):       #this block of code is to enable filter by tag
        queryset = Post.objects.all()
        query = self.request.GET.get('q')
        tag_slug = self.kwargs.get('tag_slug')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
            ).distinct()

        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = queryset.filter(tags__in=[tag])

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_slug"] = self.kwargs.get('tag_slug', None)
        return context
    
class DetailView(generic.DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'posts'
class CreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'blog/post_forms.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('list-posts')

    def form_valid(self,form):                      # Assign the current user as the author
        form.instance.author = self.request.user
        '''return self.request.user == self.get_object.author  '''
        response =  super().form_valid(form)
    # Handle new tags from input
        new_tags = self.request.POST.get('new_tags')
        if new_tags:
            tags_list = [tag.strip() for tag in new_tags.split(',')]  # Split by commas
            self.object.tags.add(*tags_list)  # Add tags to the post
        return response


class UpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    template_name = 'blog/post_forms.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('list-posts')

    def test_func(self):
        '''return self.request.user == self.get_object.author  '''
        response = self.request.user == self.get_object.author             # Ensures only the author can edit
         # Handle new tags from input
        new_tags = self.request.POST.get('new_tags')
        if new_tags:
            tags_list = [tag.strip() for tag in new_tags.split(',')]  # Split by commas
            self.object.tags.set(tags_list)  # Update tags (replacing old ones)

        return response

class DeleteView(LoginRequiredMixin,UserPassesTestMixin, generic.DeleteView):
    template_name = 'blog/post_confirm_delete.html'
    model = Post
    context_object_name = 'list-posts'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensures only the author can delete

class CommentCreateView(generic.CreateView):
    model=Comment
    form_class=CommentForm
    template_name = 'create-comment.html'
    success_url = reverse_lazy('list_comments')

class CommentListView(generic.ListView):
    model = Comment
    template_name = 'list_comment.html'
    context_object_name = 'comment'

class CommentDetailView(generic.DetailView):
    model = Comment
    template_name = 'comment_detail.html'
    context_object_name = 'comment'
class CommentUpdateView(generic.UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model=Comment
    form_class=CommentForm
    template_name = 'create-comment.html'
    success_url = reverse_lazy('list_comments')
class CommentDeleteView(generic.DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'confirm_comment_delete.html'
    success_url = 'list_comments'


class PostSearchView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) | 
                Q(tags__name__icontains=query)  # If using django-taggit
            ).distinct()
        return Post.objects.all()

