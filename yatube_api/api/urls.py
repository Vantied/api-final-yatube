from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

VERSION = 'v1'

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path(f'{VERSION}/jwt/create/',
         TokenObtainPairView.as_view(), name='jwt_create'),
    path(f'{VERSION}/jwt/refresh/',
         TokenRefreshView.as_view(), name='jwt_refresh'),
    path(
        f'{VERSION}/jwt/verify/',
        TokenVerifyView.as_view(), name='jwt_verify'),
    path(f'{VERSION}/', include(router.urls)),
]
