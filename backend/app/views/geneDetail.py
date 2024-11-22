from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.Alldata import Alldata
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import re
import os
import csv


class GeneDetailView(APIView):
    def get(self, request):
        try:
            file_headers = settings.MEDIA_ROOT
            url_headers = settings.ROOT_URL + settings.MEDIA_URL

            database_id = request.GET.get('magdb_id')

            gene_detail = Alldata.objects.filter(database_id=database_id).values('database_id', 'ncbi_gene_id', 'source', 'symbol', 'gene_type', 'aliases', 'map_location', 
                                                                          'org_name', 'tax_id', 'taxonomic_lineage', 'gene_summary').first()
            
            if gene_detail:
                gene_detail['org_name'] = re.sub(r'\(.*?\)', '', gene_detail['org_name']).strip()

            protein_detail = Alldata.objects.filter(database_id=database_id).values('transcript_protein_name', 'uniprot_id', 'pdb', 'prosite', 'interpro', 'pfam_id',
                                                                                                 'panther', 'cdd', 'protein_function', 'string').first()
            
            
            # string_val = Alldata.objects.filter(database_id=database_id).values_list('string', flat=True).first()
            if protein_detail['string']:
                protein_detail['string'] = protein_detail['string'].strip()

            string_val = protein_detail['string']
            if string_val:
                string_file_path = os.path.join(file_headers, 'image/string_image/', f'{string_val}.png')
            else:
                string_file_path = ''

            if os.path.exists(string_file_path):
                string_img = os.path.join(url_headers, 'image/string_image/', f'{string_val}.png')
            else:
                string_img = ""

            orthology_data = Alldata.objects.filter(database_id=database_id).values_list('orthology', flat=True).first()
            orthology = []
            if orthology_data:
                orthology_data = orthology_data.split('|')
                for other_id in orthology_data:
                    item = Alldata.objects.filter(database_id=other_id).values('database_id', 'symbol', 'transcript_protein_name', 'org_name', 'tax_id', 'pathway', 'ncbi_gene_id', 'uniprot_id', 'source').first()
                    item['org_name'] = re.sub(r'\(.*?\)', '', item['org_name']).strip() if item['org_name'] else ''
                    orthology.append(item)


            gene_id = Alldata.objects.filter(database_id=database_id).values_list('gene_id', flat=True).first()
            file_path = os.path.join(file_headers, 'structure&seq/Gene_expression/', f'{gene_id}.txt')
            gene_expression_data = {}
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f, delimiter='\t')  # 假设用制表符分隔
                    for _ in range(3):
                        next(f)

                    table_headers = next(reader)  # 获取表头（第三行）

                    for row in reader:
                        if len(row) == len(table_headers):  # 确保数据行与表头匹配
                            gene_expression_data = {table_headers[i]: row[i] for i in range(len(table_headers))}
            gene_expression_data = {key: value for key, value in gene_expression_data.items() if key and value}


            structure = Alldata.objects.filter(database_id=database_id).values('alphafolddb', 'pdb').first()
            alpha_pdbs = structure.get('alphafolddb')
            if alpha_pdbs:
                alpha_pdbs = alpha_pdbs.split(',')
            alpha_pdb_file_urls = []
            if alpha_pdbs:
                for item in alpha_pdbs:
                    file_path = os.path.join(file_headers, 'structure&seq/structure/Alphafold_PDB/', f'{item}.pdb')
                    if os.path.exists(file_path):
                        file_url = os.path.join(url_headers, 'structure&seq/structure/Alphafold_PDB/', f'{item}.pdb')
                        alpha_pdb_file_urls.append(file_url)
            
            pdbs = structure.get('pdb')
            if pdbs:
                pdbs = pdbs.split(',')
            pdbs_file_url = []
            if pdbs:
                for item in pdbs:
                    file_path = os.path.join(file_headers, 'structure&seq/structure/PDB/', f'{item}.pdb')
                    if os.path.exists(file_path):
                        file_url = os.path.join(url_headers, 'structure&seq/structure/PDB/', f'{item}.pdb')
                        pdbs_file_url.append(file_url)


            sequence = []
            gene_seq_path = os.path.join(file_headers, 'structure&seq/sequence/gene_sequence_all.fasta')
            if os.path.exists(gene_seq_path):
                with open(gene_seq_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.startswith('>') and gene_id == line[1:].strip():
                            sequence.append({'gene_seq': next(f).strip()})
                            break

            protein_seg_path = os.path.join(file_headers, 'structure&seq/sequence/protein_sequence_all.fasta')
            if os.path.exists(protein_seg_path):
                with open(gene_seq_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if line.startswith('>') and gene_id == line[1:].strip():
                            sequence.append({'protein_seg_path': next(f).strip()})
                            break
                                        

            # pathways = Alldata.objects.filter(database_id=database_id).values_list('kegg_pathway', flat=True).first()
            # if pathways:
            #     pathways = pathways.split(',')

            # pathway_img = []
            # if pathways:
            #     for item in pathways:
            #         pathway_img.append(url_headers + 'image/kegg_image/' + item + '.png')

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
                    'sequence': sequence,
                    'alphafold_url': alpha_pdb_file_urls,
                    'pdb_url': pdbs_file_url,
                    'orthology': orthology,
                    'gene_expression_data': gene_expression_data,
                    'string_img': string_img,
                    'external_links': external_links,
                }
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })

