from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.urls import reverse_lazy
from .forms import MyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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

class ListView:
    ...
class DetailView:
    ...
class CreateView(LoginRequiredMixin):
    ...
class UpdateView:
    ...
class DeleteView:
    ...

