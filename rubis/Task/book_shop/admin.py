from django.contrib import admin
from .models import book, review
# Register your models here.

admin.site.register(book)
admin.site.register(review)