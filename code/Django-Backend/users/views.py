from .serializers import UserAccountSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class CurrentUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 

    
    def get(self, request, *args, **kwargs):
        serializer = UserAccountSerializer(request.user)
        return Response(serializer.data)