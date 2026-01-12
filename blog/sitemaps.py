from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post

class StaticViewSitemap(Sitemap):
    """Sitemap for static pages like Home, About, and Contact"""
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        # These names must match the 'name' attribute in your urls.py
        return ['home', 'about', 'contact', 'post_list']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    """Sitemap for individual blog posts"""
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Assuming you have a field to check if post is published
        # If not, just use Post.objects.all()
        return Post.objects.all().order_by('-published_date')

    def lastmod(self, obj):
        # Returns the date the post was last updated
        return obj.published_date