from rest_framework import serializers
from .models import Thread, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('created',)


class ThreadSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = ('id', 'participants', 'created', 'updated', 'messages')
        read_only_fields = ('id', 'created', 'updated', 'messages')

    def create(self, validated_data):
        participants = validated_data.pop('participants')
        if len(participants) != 2:
            raise serializers.ValidationError('Thread can only have 2 participants.')
        thread = Thread.objects.filter(participants=participants[0]).filter(participants=participants[1]).first()
        if not thread:
            thread = Thread.objects.create()
            thread.participants.set(participants)
        return thread
