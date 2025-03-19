from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.urls import reverse_lazy
from .forms import MyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Post
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





