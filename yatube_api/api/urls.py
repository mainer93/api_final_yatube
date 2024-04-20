from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .constants import Constants
from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)
router.register('follow', FollowViewSet)

urlpatterns = [
    path(f'{Constants.VERSION}/', include(router.urls)),
    path(f'{Constants.VERSION}/', include('djoser.urls')),
    path(f'{Constants.VERSION}/', include('djoser.urls.jwt')),
]
