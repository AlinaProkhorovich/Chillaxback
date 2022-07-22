from django.contrib import admin
from core.models import Profile, Comment


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ("user", "post", "created", "active")
#     list_filter = ("active", "created", "updated")
#     search_fields = ("name", "body")


admin.site.register(Comment)
admin.site.register(Profile)
