from rest_framework import generics
from .serializer import UserSerializer
from .models import Users

# Create your views here.
class UserListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
