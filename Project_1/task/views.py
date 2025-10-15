from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Tasks
from .serializer import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend #import mới

# Create your views here.
#Get, Post
class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend] #thêm mới
    filterset_fields = ['completed','user'] #thêm mới


    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#Get, Put/Patch, Delete
class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)