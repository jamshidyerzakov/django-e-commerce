"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.auth.ouath2 import ConvertTokenView
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/api/', include('rest_framework.urls', namespace='auth-api')),
    path('admin-panel/', admin.site.urls),

    path('', include(('accounts.urls', "accounts"), namespace="account")),
    path('', include('address.urls')),
    path('', include('product.urls')),
    path('', include('category.urls')),
    path('', include('cart.urls')),
    path('', include('order.urls')),
    path('', include('service.content_type.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('rest_framework_social_oauth2.urls')),

    path('token/convert-token/', ConvertTokenView.as_view(), name="convert_token"),
 ]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
