
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Esta es la línea clave que filtra las tareas por el usuario actual
        user = self.request.user
        return Task.objects.filter(user=user)

    def perform_create(self, serializer):
        # Y esta línea asegura que la tarea se asigne al usuario actual
        serializer.save(user=self.request.user)