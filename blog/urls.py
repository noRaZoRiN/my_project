from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('detail/<int:id>/', views.post_detail, name='post_detail'),
    path('share/<int:post_id>/', views.post_share, name='post_share'),
    path('coment/<int:post_id>/',views.post_comment, name='post_comment'),
]   