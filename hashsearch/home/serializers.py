from rest_framework import serializers
from home.models import FeedElement,SearchTag

class FeedElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedElement
        fields = ['width','height','imageurl','fullimage','views']


class SearchTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchTag
        fields = ['tag','frequency']