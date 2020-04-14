
from django.contrib import admin
from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('create/',views.create, name='create'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout')
]
    # path('delete/',views.delete, name='delete'),
    # path('update/',views.update, name='update'),