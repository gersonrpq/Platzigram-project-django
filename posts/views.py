"""Posts Views"""

# Django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


class PostsFeedViews(LoginRequiredMixin, ListView):
    """Return all published post"""
    
    template_name= 'posts/feed.html'
    model=Post
    ordering=('-created',)
    paginate_by = 30
    context_object_name='posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return a post detailed"""

    template_name='posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        context['post'] = Post.objects.filter(pk=pk)[0]
        return context
    

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""

    template_name='posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

class LikePostView(LoginRequiredMixin, RedirectView):

    pattern_name = 'posts:post_detail'

    def get_redirect_url(self, *args, **kwargs):
        pk=kwargs['pk']
        post_liked = Post.objects.filter(pk=pk)[0] 
        current_user = self.request.user.profile 
        post_liked.like.add(current_user)
        return super().get_redirect_url(*args,**kwargs)   
