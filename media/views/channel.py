from rest_framework import generics
from django.db.models import Subquery, Count

from media.models import Channel
from media.serializers import ChannelSerializer



class ChannelList(generics.ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def get_queryset(self):
        return Channel.objects.all().exclude(
            id__in=Subquery(
                Channel.objects.annotate(
                    parent_count=Count('subchannels')
                ).filter(
                    parent_count__gt=0
                ).values('subchannels')
            )
        )


class ChannelDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
