from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.counter import Bacteria, Fungi, Others


class CounterView(APIView):
    def get(self, request):
        try:
            bacteria_data = Bacteria.objects.all().values()
            fungi_data = Fungi.objects.all().values()
            other_data = Others.objects.all().values()

            return Response({
                'result': 'success',
                'data': {
                    'bacteria_data': bacteria_data,
                    'fungi_data': fungi_data,
                    'other_data': other_data,
                }
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })

