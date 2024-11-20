from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.Alldata import Alldata
from django.conf import settings
import os


class StressView(APIView):
    file_headers = settings.MEDIA_ROOT
    url_headers = settings.ROOT_URL + settings.MEDIA_URL

    def get(self, request):
        try:
            pagesize = request.GET.get('pageSize', 10)
            page = request.GET.get('page', 1)

            Abiotic_path = os.path.join(self.file_headers, 'image/stress/Abiotic/')
            Biotic_path = os.path.join(self.file_headers, 'image/stress/Biotic/')
            Abiotic, Biotic = [], []
            for file_name in os.listdir(Abiotic_path):
                file_path = os.path.join(self.url_headers, 'image/stress/Abiotic/', file_name)
                name, _ = os.path.splitext(file_name)
                Abiotic.append((name, file_path))

            for file_name in os.listdir(Biotic_path):
                file_path = os.path.join(self.url_headers, 'image/stress/Biotic/', file_name)
                name, _ = os.path.splitext(file_name)
                Abiotic.append((name, file_path))

            return Response({
                'result': 'success',
                'Abiotic_stress': Abiotic,
                'Biotic': Biotic,
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })

