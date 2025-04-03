from django.contrib import admin
from django.urls import include, path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# Define the schema view with Bearer token authentication
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="API for CRUD operations",
        contact=openapi.Contact(email="poornah6@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],  # No authentication required
)

# Configure Swagger to use Bearer authentication
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version="v1",
        description="API for CRUD operations",
        contact=openapi.Contact(email="poornah6@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

# ✅ Explicitly define security scheme for "Bearer" authentication
SECURITY_SCHEMES = {
    "Bearer": {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    }
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include("student.urls")),
    path("auth/", include("users.urls")),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
