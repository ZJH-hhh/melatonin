from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Alldata
from django.conf import settings
import re


class GeneDetailView(APIView):
    def get(self, request):
        try:
            database_id = request.GET.get('magdb_id')

            gene_detail = Alldata.objects.filter(database_id=database_id).values('database_id', 'ncbi_gene_id', 'source', 'symbol', 'gene_type', 'aliases', 'map_location', 
                                                                          'org_name', 'tax_id', 'taxonomic_lineage', 'gene_summary').first()
            if gene_detail:
                gene_detail['org_name'] = re.sub(r'\(.*?\)', '', gene_detail['org_name']).strip()

            protein_detail = Alldata.objects.filter(database_id=database_id).values('transcript_protein_name', 'uniprot_id', 'pdb', 'prosite', 'interpro', 'pfam_id',
                                                                                                 'panther', 'cdd', 'protein_function', 'string').first()
            

            orthology_data = Alldata.objects.filter(database_id=database_id).values_list('orthology', flat=True).first()
            orthology = []
            if orthology_data:
                orthology_data = orthology_data.split('|')
                for other_id in orthology_data:
                    item = Alldata.objects.filter(database_id=other_id).values('database_id', 'symbol', 'transcript_protein_name', 'org_name', 'tax_id', 'pathway', 'ncbi_gene_id', 'uniprot_id', 'source').first()
                    item['org_name'] = re.sub(r'\(.*?\)', '', item['org_name']).strip()
                    orthology.append(item)

            pathways = Alldata.objects.filter(database_id=database_id).values_list('kegg_pathway', flat=True).first()
            if pathways:
                pathways = pathways.split(',')

            headers = settings.ROOT_URL + settings.MEDIA_URL + 'image/kegg_image/'
            pathway_img = []
            if pathways:
                for item in pathways:
                    pathway_img.append(headers + item + '.png')

            external_links = Alldata.objects.filter(database_id=database_id).values('kegg_id', 'kegg_pathway', 'ensembl_geneids', 'cellular_component', 'biological_process', 'molecular_function').first()
            if external_links:
                external_links['cellular_component'] = external_links['cellular_component'].split('|') if external_links['cellular_component'] else []
                external_links['biological_process'] = external_links['biological_process'].split('|') if external_links['biological_process'] else []
                external_links['molecular_function'] = external_links['molecular_function'].split('|') if external_links['molecular_function'] else []

            return Response({
                'result': 'success',
                'response': {
                    'gene_detail': gene_detail,
                    'protein_detail': protein_detail,
                    'orthology': orthology,
                    'pathways': pathway_img,
                    'external_links': external_links,
                }
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })

