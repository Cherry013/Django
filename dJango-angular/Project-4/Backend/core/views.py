from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class Registger(APIView):
    def post(self, req):
        return Response(req.data)