# coding=utf-8

from rest_framework import serializers
from .models import Record, Genre, Band, Music, Playlist

class RecordSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)


def create(self, validated_data):
    return Record.objects.create(**validated_data)


def update(self, validated_data):
    instance.title = validated_data.get('name', instance.name)
    instance.save()
    return instance


###################


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class GenreSerializer(serializers.Serializer):
    class Meta:
        model = Genre
        fields = '__all__'


class BandSerializer(serializers.Serializer):
    class Meta:
        model = Band
        fields = '__all__'


class MusicSerializer(serializers.Serializer):
    class Meta:
        model = Music
        fields = '__all__'


class PlaylistSerializer(serializers.Serializer):
    class Meta:
        model = Playlist
        fields = '__all__'
