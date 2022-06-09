from django.contrib import admin
from .models import Branch, Booking, Comment, Like

from django.contrib.contenttypes.admin import GenericStackedInline

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment


class LikeInline(GenericStackedInline):
    model = Like


# Branch에서 Comment 관리할 수 있게
class BranchAdmin(admin.ModelAdmin):
    inlines = (
        CommentInline,
        LikeInline,
    )

# Comment에서 Like 관리할 수 있게
class CommentAdmin(admin.ModelAdmin):
    inlines = (
        LikeInline,
    )


admin.site.register(Branch, BranchAdmin)
admin.site.register(Booking)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)




