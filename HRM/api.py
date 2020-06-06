""" APIVIEW consists of all basic HTTP components i.e GET,POST,UPDATE,DELETE """
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from rest_framework import status

class UserList(APIView):
    def get(self, request):
        model = Users.objects.all()
        serializer = UsersSerializer(model, many=True)
        return Response(serializer.data)
