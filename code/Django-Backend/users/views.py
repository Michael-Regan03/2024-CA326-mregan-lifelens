from .serializers import UserAccountSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CurrentUserView(viewsets.ReadOnlyModelViewSet):
    print("helloo-world")
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        print(request.user)
        serializer = UserAccountSerializer(user)
        return Response(serializer.data)