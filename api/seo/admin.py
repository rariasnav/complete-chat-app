from django.contrib import admin, messages
from .models import Sitemap, Article, ArticleVersion, Suggestion
from .tasks import async_create_article_from_sitemap
from .actions import suggest_changes_to_article

@admin.register(Sitemap)
class SitemapAdmin(admin.ModelAdmin):
    list_display = ("url", "user", "created_at", "updated_at", "last_sync")
    list_filter = ("user", "created_at", "updated_at", "last_sync")
    search_fields = ("url", "user__username")

    def _async_create_article_from_sitemap(self, request, queryset):
        for sitemap in queryset:
            async_create_article_from_sitemap.delay(sitemap.url)

    actions = [_async_create_article_from_sitemap]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "sitemap", "created_at", "updated_at", "language", "slug")
    list_filter = ("sitemap", "created_at", "updated_at", "language")
    search_fields = ("title", "description", "keywords", "slug")
    actions = ['suggest_changes']
    def suggest_changes(self, request, queryset):
        for a in queryset:
            suggestions = suggest_changes_to_article(a.id)
            self.message_user(request, f"Suggestions for '{a.title}': {suggestions}", messages.INFO)
    suggest_changes.short_description = "Suggest changes to selected articles"

# Register your models here.
@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ("article", "original_text", "replacement_text", "created_at", "updated_at")
    list_filter = ("article", "created_at", "updated_at")
    search_fields = ("original_text", "replacement_text", "keywords")


@admin.register(ArticleVersion)
class ArticleVersionAdmin(admin.ModelAdmin):
    list_display = ("article", "version_number", "created_at", "updated_at")
    list_filter = ("article", "created_at", "updated_at")
    search_fields = ("article__title", "keywords")