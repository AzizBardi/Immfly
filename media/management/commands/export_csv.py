import csv
from django.core.management.base import BaseCommand
from django.db.models import Subquery, Count

from media.models import Channel
from media.serializers import ChannelSerializer


class Command(BaseCommand):
    help = 'Export Content objects to a CSV file'

    def handle(self, *args, **options):
        filename = 'content.csv'
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['title', 'rating']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            channels_queryset = Channel.objects.all().exclude(
                id__in=Subquery(
                    Channel.objects.annotate(
                        parent_count=Count('subchannels')
                    ).filter(
                        parent_count__gt=0
                    ).values('subchannels')
                )
            )
            channels_serialize = ChannelSerializer(data=channels_queryset,many=True)
            channels_serialize.is_valid()
            sorted_list = sorted(channels_serialize.data, key=lambda x: x['rating'], reverse=True)
            for obj in sorted_list:
                writer.writerow({
                    'title': obj["title"],
                    'rating': obj["rating"],
                })

