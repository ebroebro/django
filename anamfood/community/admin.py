from django.contrib import admin
from .models import Community, Comment

# Register your models here.
class CommunityAdmin(admin.ModelAdmin):
    list_display=('pk','title','store_name','rank','content','created_at','updated_at')

class CommentAdmin(admin.ModelAdmin):
    list_display=('pk','user','contnet','created_at')

admin.site.register(Community)
admin.site.register(Comment)