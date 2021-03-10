from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from blog.models import Category, Post, Comment
from django import template
from django.views import generic
from blog.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db import models
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from .filters import PostFilter
from django.db.models import Q
from operator import attrgetter


# Create your views here.
@login_required
def index(req):
    #post_latest = Post.objects.order_by("-createDate")[:10]
    #context={
        #"post_latest" : post_latest,
    #}
    context = {}

    query= ""
    if req.GET:
        query = req.GET['q']
        context['query'] =str(query)

    post_latest=sorted(get_blog_queryset(query), key=attrgetter("createDate"), reverse=True)
    context['post_latest'] = post_latest
    
    return render(req, "index.html", context=context)

#def single(req):
    #context={}
    #return render(req, "single.html", context=context)


class PostDetailView(generic.DetailView, LoginRequiredMixin):
    model=Post




class PostCreate(LoginRequiredMixin, CreateView):
    model=Post
    fields=["title", "tentative_title","category", "inci_name", "ingredient", "export_china", "thesis", "thesis_name", "patent","patent_number", "reward", "reward_name","content", "title_image", "efficacy_image"]

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model=Post
    fields=["title", "tentative_title","category","inci_name","ingredient", "export_china", "thesis", "thesis_name", "patent","patent_number", "reward", "reward_name", "content", "title_image", "efficacy_image"]

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(generic.DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False 

class AddCommentView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model=Post
    form_class=CommentForm
    template_name='add_comment.html'

    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    success_url=reverse_lazy('index')

def get_blog_queryset(query=None):
    queryset=[]
    queries=query.split(" ")
    for q in queries:
        posts=Post.objects.filter(
            Q(title__icontains=q) |
            Q(category__name__icontains=q) |
            Q(author__username__icontains=q) |
            Q(tentative_title__icontains=q) |
            Q(inci_name__icontains=q) |
            Q(ingredient__icontains=q) |
            Q(thesis_name__icontains=q) |
            Q(patent_number__icontains=q) |
            Q(reward_name__icontains=q) 
        ).distinct()

        for post in posts:
            queryset.append(post)
    return list(set(queryset))

@login_required
def favourite_post(request, id):
    post=get_object_or_404(Post, id=id)
    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
    else:
        post.favourite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def favourite_list(request):
    new = Post.objects.filter(favourite=request.user)
    return render(request, 'favourites.html', {'new': new})

@login_required
def blog_list(request):
    blogs=Post.objects.all()
    blogs_list=blogs.filter(author=request.user)
    context={
        'blogs_list': blogs_list,
    }
    return render(request, 'mypost.html', context)
