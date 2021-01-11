from .models import Post

def recent_posts_to_context(request):
    return {
        'recent_posts': Post.objects.filter(status=1).order_by('-created_on')[:3]
    }