from django.urls import path

from .views import PerevalCreateAPIView, PerevalRetrieveAPIView, PerevalRetrieveUpdateAPIView, PerevalListAPIView

urlpatterns = [
    path('submitData/create', PerevalCreateAPIView.as_view()),
    path('submitData/<int:pk>', PerevalRetrieveAPIView.as_view()),
    path('submitData/<int:pk>/update', PerevalRetrieveUpdateAPIView.as_view()),
    path('submitData/<str:email>', PerevalListAPIView.as_view()),
]
