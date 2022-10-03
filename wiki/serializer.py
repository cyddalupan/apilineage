from rest_framework import serializers

from .models import WikiBase, WikiContent

class WikiBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WikiBase
        fields = "__all__"


class WikiContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WikiContent
        fields = "__all__"