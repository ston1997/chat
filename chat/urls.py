from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    ThreadListCreateView, MessageListView, read_message,
    unread_count, CustomTokenObtainPairView
)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('threads/', ThreadListCreateView.as_view(), name='thread_list_create'),
    path('threads/<int:thread_id>/messages/', MessageListView.as_view(), name='message_list'),
    path('messages/read/', read_message, name='read_message'),
    path('messages/unread/count/', unread_count, name='unread_count'),
]
