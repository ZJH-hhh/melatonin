from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.Alldata import Alldata
from django.core.paginator import Paginator
import re

class SpeciesDetailView(APIView):
    def get(self, request):
        try:
            tax_id = request.GET.get('tax_id')
            pagesize = request.GET.get('pageSize', 10)
            page = request.GET.get('page', 1)

            data = Alldata.objects.filter(tax_id=tax_id).values('database_id', 'symbol', 'transcript_protein_name', 'org_name', 'tax_id', 'pathway', 'ncbi_gene_id', 'uniprot_id', 'source').order_by('database_id')

            paginator = Paginator(data, pagesize)

            current_page = paginator.page(page)
            res = list(current_page.object_list)

            for item in res:
                item['org_name'] = re.sub(r'\(.*?\)', '', item['org_name']).strip()

            return Response({
                'result': 'success',
                'total': len(data),
                'data': res
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })

