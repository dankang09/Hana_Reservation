from django.contrib import admin
from .models import Branch, Booking, Comment, Like


# Register your models here.

admin.site.register(Branch)
admin.site.register(Booking)
admin.site.register(Comment)
admin.site.register(Like)