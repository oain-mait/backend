from rest_framework import generics
from rest_framework.permissions import AllowAny

from back_app.serializers import *


class FinalView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = FinalProjectSerializer
