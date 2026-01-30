from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view["POST"]
def create_user(request):
    return Response(request.body, status=status.HTTP_201_CREATED)