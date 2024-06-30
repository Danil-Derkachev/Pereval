from django.urls import path

from .views import PerevalCreateAPIView, PerevalRetrieveAPIView, PerevalRetrieveUpdateAPIView

urlpatterns = [
    path('submitData/create', PerevalCreateAPIView.as_view()),
    path('submitData/<int:pk>', PerevalRetrieveAPIView.as_view()),
    path('submitData/<int:pk>/update', PerevalRetrieveUpdateAPIView.as_view()),
]
