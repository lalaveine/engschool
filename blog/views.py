from django.shortcuts import render
from django.views.generic import ListView
from hitcount.views import HitCountDetailView
from .models import Post


class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Blog'
        return context


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'post_detail.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Blog'
        context['popular_posts'] = Post.objects.order_by('hit_count_generic')[:5]
        return context
