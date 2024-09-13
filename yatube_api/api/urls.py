from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (
    CommentViewSet,
    FollowCreateListViewSet,
    GroupViewSet,
    PostViewSet
)

app_name = 'posts'

router_v1 = SimpleRouter()

router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(
    r'posts/(?P<post_pk>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('follow', FollowCreateListViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
