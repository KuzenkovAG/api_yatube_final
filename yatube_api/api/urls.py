from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'posts', views.PostViewSet, basename='Post')
router.register(r'groups', views.GroupViewSet, basename='Group')
router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    views.CommentViewSet,
    basename='Comment'
)

urlpatterns = [
    path('v1/follow/', views.FollowView.as_view()),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
