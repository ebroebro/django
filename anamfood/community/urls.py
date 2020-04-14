from django.contrib import admin
from django.urls import path
from . import views

app_name='community'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/update/',views.update, name='update'),
    path('create/',views.create,name='create')
]
