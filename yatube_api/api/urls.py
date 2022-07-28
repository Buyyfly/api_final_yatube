from django.views.generic import TemplateView
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CommentViewSet, FollowViewSet,
                    GroupViewSet, PostViewSet)


router = SimpleRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('djoser.urls.jwt')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
