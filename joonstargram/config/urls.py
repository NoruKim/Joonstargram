from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
# from django.contrib.auth.models import User
from joonstargram.users.models import User
from joonstargram.posts.views import PostViewSet
from joonstargram.users.views import UserViewSet, HelloWorldAPI
from rest_framework import routers, serializers, viewsets

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("api/", include("joonstargram.users.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #login, registration등 path 설정
    path("api/rest-auth/", include("rest_auth.urls")),
    # 토큰 발급 및 재발급 페이지 설정
    path('api/rest-auth/obtain_token/', obtain_jwt_token, name="obtain-jwt"),
    path('api/rest-auth/refresh_token/', refresh_jwt_token, name="refresh-jwt"),
    path('api/hello', HelloWorldAPI.as_view()),
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    # path("", include("joonstargram.users.urls", namespace="users")),
    # /posts/
    path("posts/", include("joonstargram.posts.urls", namespace="posts")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
