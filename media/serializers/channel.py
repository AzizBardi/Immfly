from rest_framework import serializers
from media.serializers.content import ContentSerializer
from media.models import Channel
from media.utils.channel import calculate_rating


class ChannelSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)
    rating = serializers.FloatField(required=False, default=0)
    subchannels = serializers.SerializerMethodField()

    def get_subchannels(self, obj):
        subchannels = obj.subchannels.all()
        serializer = ChannelSerializer(subchannels, many=True)
        return serializer.data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        rating = calculate_rating(instance)
        data['rating'] = rating
        return data

    class Meta:
        model = Channel
        fields = ('id', 'title', 'language', 'picture', 'contents', 'subchannels', 'slug', 'rating')
