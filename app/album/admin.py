from django.contrib import admin
from album.models import PhotoBook, Photo


@admin.register(PhotoBook)
class PhotoBookAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass