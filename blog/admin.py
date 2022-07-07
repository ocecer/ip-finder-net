from django.contrib import admin
from.models import Blog, Category
from django.utils.safestring import mark_safe

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_verified", "is_featured", "blog_category",)
    list_editable = ("is_verified", "is_featured",)
    search_fields = ("title", "description",)
    # list_filter = ("is_verified", "category",)
    list_filter = ("is_verified","categories",)

    def blog_category(self, obj):
        html = "<ul>"

        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"

        html += "</ul>"
        return mark_safe(html) 


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
