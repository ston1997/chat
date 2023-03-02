from rest_framework import generics, status, serializers
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Thread, Message, User
from .serializers import ThreadSerializer, MessageSerializer


class ThreadListCreateView(generics.ListCreateAPIView):
    serializer_class = ThreadSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Thread.objects.filter(participants=self.request.user)


class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        thread_id = self.kwargs['thread_id']
        return Message.objects.filter(thread_id=thread_id)


@api_view(['POST'])
def read_message(request):
    message_ids = request.data.get('message_ids', [])
    Message.objects.filter(id__in=message_ids).update(is_read=True)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def unread_count(request):
    unread_count = Message.objects.filter(thread__participants=request.user, is_read=False).count()
    return Response({'unread_count': unread_count})


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = User.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            raise serializers.ValidationError('Invalid credentials.')
        attrs['user'] = user
        return attrs

    def get_token(self, user):
        token = super().get_token(user)
        token['name'] = user.name
        token['email'] = user.email
        return token
