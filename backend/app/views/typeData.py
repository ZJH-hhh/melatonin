from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Alldata
from django.core.paginator import Paginator
from django.conf import settings
import re

class TypeDataView(APIView):
    def get(self, request):
        try:
            type = request.GET.get('type')
            pagesize = request.GET.get('pageSize', 10)
            page = request.GET.get('page', 1)

            # print(request.GET)

            typedata = Alldata.objects.filter(taxonomic_groups=type).values('database_id', 'org_name', 'tax_id')
        
            headers = settings.ROOT_URL + settings.MEDIA_URL + 'image/species/'
            unique_data = {}
            for item in typedata:
                tax_id = item['tax_id']
                if tax_id not in unique_data:
                    item['photo_url'] = headers + str(tax_id) + '.jpg'
                    item['org_name'] = re.sub(r'\s*\(.*?\)\s*', ' ', item['org_name']).strip()
                    unique_data[tax_id] = item

            unique_data = list(unique_data.values())
            paginator = Paginator(unique_data, pagesize)
            
            current_page = paginator.page(page)
            data = list(current_page.object_list)

            return Response({
                'result': 'success',
                'total': len(unique_data),
                'data': data
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })