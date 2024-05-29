from django.contrib.sitemaps import Sitemap

from core.models import Author


class AuthorSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Author.objects.all().order_by("name")

    def lastmod(self, obj: Author):
        return obj.updated_at
