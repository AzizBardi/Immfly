from rest_framework import generics

from media.models import AudioLanguage, Content
from media.serializers import AudioLanguageSerializer, ContentSerializer


class AudioLanguageList(generics.ListAPIView):
    queryset = AudioLanguage.objects.all()
    serializer_class = AudioLanguageSerializer


class AudioLanguageDetail(generics.RetrieveAPIView):
    queryset = AudioLanguage.objects.all()
    serializer_class = AudioLanguageSerializer


class ContentList(generics.ListAPIView):
    queryset = Content.objects.select_related('subtitlelanguage_set', 'audiolanguage_set')
    serializer_class = ContentSerializer


class ContentDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
