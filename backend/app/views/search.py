from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Alldata

class SearchView(APIView):
    def get(self, request):
        try:
            type = request.GET.get('searchType')
            value = request.GET.get('value')
            filter = {type: value}
            data = Alldata.objects.filter(**filter).values()
            return Response({
                'result': 'success',
                'data': data
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })
        