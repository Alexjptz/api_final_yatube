from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet, basename='post_list')
v1_router.register(
    'posts/(?P<post_id>[0-9]+)/comments',
    CommentViewSet,
    basename='comment_list'
)
v1_router.register('group', GroupViewSet, basename='group-list')
v1_router.register('follow', FollowViewSet, basename='follow-list')

auth_patterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh', TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/token/', include(auth_patterns)),
]
