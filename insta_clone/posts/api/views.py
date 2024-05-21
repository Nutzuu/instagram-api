from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework.generics import ListAPIView # type: ignore
from ..models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class UserPostsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        posts = Post.objects.filter(users_whom_liked=user)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostCommentsAPIView(ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

