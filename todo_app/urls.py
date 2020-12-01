from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token

from .api import router

v = settings.API_VERSION

urlpatterns = [
    path('admin/', admin.site.urls),

    # API
    # Auth endpoints
    path('api/' + v + '/auth/refresh/', refresh_jwt_token, name='refresh_jwt_token'),
    path('api/' + v + '/auth/token/', obtain_jwt_token, name='obtain_jwt_token'),
    # Router endpoints
    path('api/' + v + '/', include(router.urls), name='api'),
    # only for test purposes
    path('api-auth/', include('rest_framework.urls'), name='rest_framework')
]
