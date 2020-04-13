from django.contrib import admin
from .models import Reviews


# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display=('title','restaurant','rank','content','created_at','updated_at')

admin.site.register(Reviews)