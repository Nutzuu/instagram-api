from django.urls import path
from .api.views import UserPostsAPIView, PostCommentsAPIView

app_name = "posts"
urlpatterns = [
    path('', UserPostsAPIView.as_view(), name='user-posts'),
    path('<int:post_id>/comments/', PostCommentsAPIView.as_view(), name='post-comments'),
]
