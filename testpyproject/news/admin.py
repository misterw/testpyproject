from django.contrib import admin

from testpyproject.news.models import News


class NewsAdmin(admin.ModelAdmin):
    model = News
    list_display = ('title', 'datetime')
    search_fields = (
        'title',
    )
    list_per_page = 20

    fieldsets = (
        ('Edit news', {
            'fields': ('title', 'datetime', 'content')
        }),
    )


admin.site.register(News, NewsAdmin)

