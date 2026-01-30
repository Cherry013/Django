from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        #fileds = "__all__"
        fields = ['id', 'first_name', 'last_name', 'email', 'password']