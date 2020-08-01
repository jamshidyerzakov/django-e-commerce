from django.urls import path
from .views import ContentTypeView


urlpatterns = [
    path('content_type/', ContentTypeView.as_view())
]
