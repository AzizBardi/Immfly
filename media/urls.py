from django.urls import path
from media.views import ChannelList, ChannelDetail
from media.views import (
    ContentDetail,
)

urlpatterns = [
    path('channels/', ChannelList.as_view(), name='channel-list'),
    path('channels/<str:slug>/', ChannelDetail.as_view(), name='channel-detail'),
    path('contents/<str:slug>/', ContentDetail.as_view(), name='content-detail'),
]

