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
    path('create/',views.create,name='create'),
    path('<int:pk>/map/',views.map, name='map'),
    path('<int:pk>/map2/',views.map2,name='map2'),
    path('<int:community_pk>/comment/', views.create_comment, name='create_comment'),
    path('<int:community_pk>/comment/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment')
]

#