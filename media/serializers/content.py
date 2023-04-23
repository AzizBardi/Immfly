from rest_framework import serializers

from media.models import SubtitleLanguage, AudioLanguage, Content


class SubtitleLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubtitleLanguage
        fields = ('id', 'name', 'file')

class AudioLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioLanguage
        fields = ('id', 'name', 'file')

class ContentSerializer(serializers.ModelSerializer):
    subtitle_languages = serializers.SerializerMethodField()
    audio_languages = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = ('id', 'title', 'description', 'author', 'genre', 'rating', 'file', 'type','slug',
                  'subtitle_languages','audio_languages')

    def get_subtitle_languages(self, obj):
        subtitle_languages = obj.subtitlelanguage_set.all()
        return SubtitleLanguageSerializer(subtitle_languages, many=True).data

    def get_audio_languages(self, obj):
        audio_languages = obj.audiolanguage_set.all()
        return AudioLanguageSerializer(audio_languages, many=True).data