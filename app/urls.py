from django.urls import path
from .views import (
    translate_view, translate_api,
)

app_name = 'app'

urlpatterns = [
    path('translate/', translate_view,
         name='translate'),
    path('translate_api/', translate_api),
]