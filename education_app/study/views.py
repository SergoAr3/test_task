from rest_framework import generics
from .models import CheckView
from .serializers import CheckViewSerializer

class LessonListView(generics.ListAPIView):
    serializer_class = CheckViewSerializer

    def get_queryset(self):
        user = self.request.user
        return CheckView.objects.filter(user=user)