from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Friends
from .Serializer import FriendSerializer


# @api_view["POST"]
# def create_user(request):
#     return Response(request.body, status=status.HTTP_201_CREATED)

class FriendsAPI(APIView):
    def get(self, request):
        friends = Friends.objects.all()
        serializer = FriendSerializer(friends, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = FriendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)