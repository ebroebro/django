from django.contrib import admin
from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/follow/', views.follow, name='follow')
]
