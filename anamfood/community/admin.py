from django.contrib import admin
from .models import Community

# Register your models here.
class CommunityAdmin(admin.ModelAdmin):
    list_display=('pk','title','store_name','rank','content','created_at','updated_at')

admin.site.register(Community)