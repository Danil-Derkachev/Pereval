from django.http import JsonResponse
from rest_framework import generics

from .models import Pereval
from .serializers import PerevalSerializer


class PerevalAPI(generics.CreateAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def post(self, request):
        pereval = PerevalSerializer(data=request.data)
        try:
            if pereval.is_valid(raise_exception=True):
                pereval.save()
                data = {'status': '200', 'message': 'null', 'id': f'{pereval.instance.id}'}
                return JsonResponse(data, status=200, safe=False)

        except Exception as exc:
            response_data = {'status': '400', 'message': f'Bad Request: {exc}', 'id': 'null'}
            return JsonResponse(response_data, status=400, safe=False)
