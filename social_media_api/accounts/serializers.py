from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        user = User
        fields = ['bio', 'profile_picture', 'followers']