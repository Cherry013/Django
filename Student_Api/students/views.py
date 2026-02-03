from rest_framework.schemas.coreapi import is_custom_action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializer


class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.filter(is_active=True)
        data = {
            "count":students.count(),
            "data":StudentSerializer(students, many=True).data
        }
        return Response(data)

    def post(self, request):
        serializer =StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Student, pk=pk, is_active=True)

    def get(self, request, pk):
        serializer = StudentSerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = StudentSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        serializer = StudentSerializer(self.get_object(pk), data=request.data, partial=True)
        if serializer.is_vaid():
            serializer.save()
            msg = {
                "message": "Student updated successfully",
                "data": serializer.data
            }
            return Response(msg, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.is_active = False
        student.save()
        # self.get_object(pk).delete() # We shouldn't delete these things we just make them inactive major companies follow these
        return Response({"Message": "Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)


# class StudentDetailAPIView(APIView):
#     def get(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         student.delete()
#         msg = f"{student.name} with id : {pk} "+"Deleted"
#         return Response({"Message":msg}, status=204)


# Generic_APIs
class StudentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, pk):
        super().delete(request, pk)
        return Response({"Message": "Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)


# Industry Strandard
# HTTP Method → DRF Action → ORM
# GET(list) → queryset.all()
# GET(pk) → get(pk)
# POST → serializer.save()
# PUT/PATCH → update()
# DELETE → delete()
class StudentInd(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer