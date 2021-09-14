from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import *
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'posts': Post.objects.all(),
        'comments': Comment.objects.all(),
    }
    return render(request,'blog/home.html',context)

def postlist(request):
    if request.method == 'GET':
        query = request.GET.get('query','')
        post = Post.objects.filter(title__icontains=query).order_by('-date_posted') 
        p = Paginator(post,3)
        page = request.GET.get('page')
        posts = p.get_page(page)
        nums = "a" * posts.paginator.num_pages
        context = {
            'posts':posts,
            'nums':nums,
            'query':query,
        }
        return render(request,'blog/home.html',context )

def username(request):
    if request.method == 'GET':
        query = request.GET.get('query','')
        post = Post.objects.filter(title__icontains=query).order_by('author__username') 
        p = Paginator(post,3)
        page = request.GET.get('page')
        posts = p.get_page(page)
        nums = "a" * posts.paginator.num_pages
        context = {
            'posts':posts,
            'nums':nums,
            'query':query,
        }
        return render(request,'blog/home.html',context )    

def postitle(request):
    if request.method == 'GET':
        query = request.GET.get('query','')
        post = Post.objects.filter(title__icontains=query).order_by('title') 
        p = Paginator(post,3)
        page = request.GET.get('page')
        posts = p.get_page(page)
        nums = "a" * posts.paginator.num_pages
        context = {
            'posts':posts,
            'nums':nums,
            'query':query,
        }
        return render(request,'blog/home.html',context )    

def oldpostlist(request):
    if request.method == 'GET':
        query = request.GET.get('query','')
        post = Post.objects.filter(title__icontains=query).order_by('date_posted') 
        p = Paginator(post,3)
        page = request.GET.get('page')
        posts = p.get_page(page)
        nums = "a" * posts.paginator.num_pages
        context = {
            'posts':posts,
            'nums':nums,
            'query':query,
        }
        return render(request,'blog/home.html',context )

# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 3
    
#     def get_queryset(self):
#         query = self.request.GET.get('query','')
#         posts = Post.objects.all().order_by('-date_posted')
#         if query:
#             posts = Post.objects.filter(title__icontains=query).order_by('-date_posted')
#         else:
#             posts = Post.objects.all().order_by('-date_posted')
#         return posts
        
        

class UserPostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetialView(LoginRequiredMixin,DetailView):
    model = Post

class UserDetialView(LoginRequiredMixin,DetailView):
    model = User
    template_name = 'blog/user_detial.html'

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    fields = ['content',]

    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        comment = self.get_object()
        id=comment.post_id
        return reverse_lazy('post-detial', kwargs={'pk': id})

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

class CommentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Comment
    fields = ['content',]

    def form_valid(self,form):
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False



class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def about(request):
    return render(request,'blog/about.html',{'title': 'About'})


def login(request):
    return render(request,'blog/.html')