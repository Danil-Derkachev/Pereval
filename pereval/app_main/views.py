from django.http import JsonResponse
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView

from .models import Pereval
from .serializers import PerevalCreateSerializer, PerevalRetrieveSerializer, PerevalRetrieveUpdateSerializer


class PerevalCreateAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        pereval = PerevalCreateSerializer(data=request.data)
        try:
            if pereval.is_valid(raise_exception=True):
                pereval.save()
                data = {'status': '200', 'message': 'null', 'id': f'{pereval.instance.id}'}
                return JsonResponse(data=data)

        except Exception as exc:
            data = {'status': '400', 'message': f'Bad Request: {exc}', 'id': 'null'}
            return JsonResponse(data=data)


class PerevalRetrieveAPIView(RetrieveAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalRetrieveSerializer


class PerevalRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalRetrieveUpdateSerializer

    def patch(self, request, *args, **kwargs):
        instance = Pereval.objects.get(pk=kwargs['pk'])
        if instance.status != "NE":
            data = {"state": 0, "message": "Перевал на модерации, вы не можете его изменить."}
            return JsonResponse(data=data)
        else:
            serializer = PerevalRetrieveUpdateSerializer(data=request.data, instance=instance)
            try:
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    data = {"state": 1, "message": "null"}
                    return JsonResponse(data=data)
            except Exception as exc:
                data = {"state": 0, "message": f"Bad Request: {exc}"}
                return JsonResponse(data=data)
