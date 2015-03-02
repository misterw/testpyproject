from django.contrib import admin
from testpyproject.python_game.models import PythonGameResult
from django.core.urlresolvers import reverse


class PythonGameAdmin(admin.ModelAdmin):
    model = PythonGameResult
    list_display = ('game_date', 'score', 'user_link')
    list_per_page = 20

    fieldsets = (
        ('Result info', {
            'fields': ('game_date', 'score', 'user_link')
        }),
    )
    readonly_fields = ('game_date', 'score', 'user_link')

    def get_actions(self, request):
        return False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def user_link(self, instance):
        url = reverse('admin:%s_%s_change' % ('auth', 'user'), args=(instance.user_id,))
        return '<a href="%s" target="_blank">%s</a>' % (url, instance.user.username)
    user_link.allow_tags = True
    user_link.admin_order_field = 'user__id'
    user_link.short_description = 'User'


admin.site.register(PythonGameResult, PythonGameAdmin)
