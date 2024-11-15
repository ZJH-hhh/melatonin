from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.Alldata import Alldata
from django.core.paginator import Paginator
import re
from django.db.models import Q


class SearchView(APIView):
    field_mapping = {
            'MAGEdb ID': 'database_id',
            'NCBI gene ID': 'ncbi_gene_id',
            'Gene name': 'symbol',
            'Protein name': 'transcript_protein_name',
            'Organism': 'org_name',
            'Taxonomy ID': 'tax_id',
            'Plant Growth': 'plant_growth',
            'Stress name': 'stress',
            'Disease name': 'disease',
            'Stage of life cycle': 'animal_growth',
            'Pathway component': 'pathway'
        }
    
    
    def get(self, request):
        try:
            search_type1 = request.GET.get('searchType1')
            value1 = request.GET.get('value1')
            search_type2 = request.GET.get('searchType2')
            value2 = request.GET.get('value2')
            method = request.GET.get('method')
            pagesize = request.GET.get('pageSize', 10)
            page = request.GET.get('page', 1)

            print(search_type1, search_type2)

            key1 = self.field_mapping.get(search_type1)
            key2 = self.field_mapping.get(search_type2)

            if method == 'and':
                filter_criteria = {key1: value1, key2: value2}
                data = Alldata.objects.filter(**filter_criteria)
            elif method == 'or':
                filter_criteria = Q(**{key1: value1}) | Q(**{key2: value2})
                data = Alldata.objects.filter(filter_criteria)
            else:
                filter_criteria = {key1: value1}
                data = Alldata.objects.filter(**filter_criteria)
            
            data = data.values('database_id', 'symbol', 'transcript_protein_name', 'org_name', 'tax_id', 'pathway', 'ncbi_gene_id', 'uniprot_id', 'source').order_by('database_id')
            paginator = Paginator(data, pagesize)

            current_page = paginator.page(page)
            res = list(current_page.object_list)

            for item in res:
                item['org_name'] = re.sub(r'\(.*?\)', '', item['org_name']).strip()

            return Response({
                'result': 'success',
                'total': paginator.count,
                'data': res
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })
        