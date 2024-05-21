from rest_framework import status # type: ignore
from rest_framework import generics # type: ignore
from rest_framework.decorators import action # type: ignore
from rest_framework.mixins import ListModelMixin # type: ignore
from rest_framework.mixins import RetrieveModelMixin # type: ignore
from rest_framework.mixins import UpdateModelMixin # type: ignore 
from rest_framework.response import Response # type: ignore
from rest_framework.viewsets import GenericViewSet # type: ignore 
from rest_framework.permissions import AllowAny # type: ignore
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView # type: ignore
from rest_framework.authtoken.models import Token #type: ignore

from insta_clone.users.models import User

from .serializers import UserSerializer
from .serializers import UserSerializer, RegisterSerializer

class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        print('Trying to register')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # get the token here
            token, created = Token.objects.get_or_create(user=user)
            return Response({"username": user.username, "email": user.name, "token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

