from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.Alldata import Alldata
from django.core.paginator import Paginator
import re

class SpeciesDetailView(APIView):
    def get(self, request):
        try:
            tax_id = request.GET.get('tax_id')
            pathway = request.GET.get('pathway')
            species_type = request.GET.get('species_type')
            animal_growth = request.GET.get('animal_growth')
            plant_growth = request.GET.get('plant_growth')
            disease = request.GET.get('disease')
            stress = request.GET.get('stress')
            pagesize = request.GET.get('pageSize', 10)
            page = request.GET.get('page', 1)

            if tax_id:
                queryset = Alldata.objects.filter(tax_id=tax_id)
            elif animal_growth:
                queryset = Alldata.objects.filter(animal_growth__contains=animal_growth)
            elif plant_growth:
                queryset = Alldata.objects.filter(plant_growth__contains=plant_growth)
            elif disease:
                queryset = Alldata.objects.filter(disease__contains=disease)
            elif stress:
                queryset = Alldata.objects.filter(stress__contains=stress)
            elif pathway and type:
                queryset = Alldata.objects.filter(pathway__contains=pathway, taxonomic_groups=species_type)
                
            data = queryset.values('database_id', 'symbol', 'transcript_protein_name', 'org_name', 'tax_id', 'pathway', 'ncbi_gene_id', 'uniprot_id', 'source').order_by('database_id')
            
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

