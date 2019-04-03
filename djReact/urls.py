from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from inventory.views import ReactAppView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('api/', include('article.api.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path('.*', ReactAppView.as_view())
]
