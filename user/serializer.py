from rest_framework import serializers

from .models import MemberUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberUser
        fields = "__all__"
