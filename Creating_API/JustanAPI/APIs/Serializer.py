from rest_framework import serializers

from .models import Friends


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'


# # Basic Serializer
# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     email = serializers.EmailField()
#     age = serializers.IntegerField(required=False)


# # Field Level Serializer
# class UserSerializer(serializers.Serializer):
#     age = serializers.IntegerField()
#
#     def validate_age(self, value):
#         if value < 0:
#             raise serializers.ValidationError("Must be adult")
#         return value

# # Object level Serializer
# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()
#     confirm_password = serializers.CharField()
#
#     def validate_password(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError('Passwords must match')
#         return data


# Model Serializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"