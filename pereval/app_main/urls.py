from django.urls import path

from .views import PerevalAPI


urlpatterns = [
    path('submitData', PerevalAPI.as_view()),
]
