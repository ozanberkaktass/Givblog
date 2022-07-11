from pickle import OBJ
from django.contrib import admin
from .models import Blog, Category, navbar
from django.utils.safestring import mark_safe
from django.conf.locale.es import formats as es_formats


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug","is_day","selected_categories",)
    list_editable = ("is_active","is_home","is_day")
    search_fields = ("title","description",)
    readonly_fields = ("slug",)
    list_filter=("is_active","is_home","categories")


    es_formats.DATETIME_FORMAT = "d M Y H:i"
    def selected_categories(self,obj):
        html="<ul>"
        for category in obj.categories.all():
            html+="<li>" + category.name + "</li> "

        html+="</ul>"
        return mark_safe(html)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(navbar)
