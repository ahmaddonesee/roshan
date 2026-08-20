from django.contrib import admin
from .models import UploadFile,Comment


@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):
    list_display = ('name','author')
    search_fields = ['name']
    
    class Meta:
        verbose_name_plural="ادمین"
    
    
@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display=['user']
    