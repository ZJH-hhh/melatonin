from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from app.models import Alldata
import json

class TestView(APIView):
    def get(self, request):
        try:
            data = Alldata.objects.first()
            data = json.loads(serializers.serialize("json", [data]))[0]
            return Response({
                'result': 'success',
                'data': data['fields']
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })