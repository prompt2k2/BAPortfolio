from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post

class LatestPostsFeed(Feed):
    title = "Business Analyst Blog"
    link = "/blog/"
    description = "Latest articles from Business Analyst Blog"
    
    def items(self):
        return Post.objects.filter(status='published').order_by('-published_date')[:10]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.excerpt
    
    def item_link(self, item):
        return reverse('post_detail', args=[item.slug])
    
    def item_pubdate(self, item):
        return item.published_date