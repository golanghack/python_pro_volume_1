from rest_framework_nested import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet
from core.post.viewsets import PostViewSet
from core.comment.viewsets import CommentViewSet

router = routers.SimpleRouter()

# auth
router.register(r'api/auth/register', RegisterViewSet, basename='auth-register')
router.register(r'api/auth/login', LoginViewSet, basename='auth-login')
router.register(r'api/auth/refresh', RefreshViewSet, basename='auth-refresh')

# User
router.register(r'user', UserViewSet, basename='user')

# Post
router.register(r'post', PostViewSet, basename='post')
posts_router = routers.NestedSimpleRouter(router, r'post', lookup='post')
posts_router.register(r'comment', CommentViewSet, basename='post-comment')

urlpatterns = [
    *router.urls,
    *posts_router.urls,
]