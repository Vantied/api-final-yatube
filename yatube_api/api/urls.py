from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

VERSION = 'v1'

app_name = 'api'

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path(f'{VERSION}/jwt/create/',
         TokenObtainPairView.as_view(), name='jwt_create'),
    path(f'{VERSION}/jwt/refresh/',
         TokenRefreshView.as_view(), name='jwt_refresh'),
    path(
        f'{VERSION}/jwt/verify/',
        TokenVerifyView.as_view(), name='jwt_verify'),
    path(f'{VERSION}/', include(router_v1.urls)),
]
