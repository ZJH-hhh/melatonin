# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alldata(models.Model):
    database_id = models.CharField(db_column='Database_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data_id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    gene_type = models.CharField(db_column='Gene_Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tax_id = models.IntegerField(blank=True, null=True)
    gene_summary = models.TextField(db_column='Gene_summary', blank=True, null=True)  # Field name made lowercase.
    map_location = models.CharField(db_column='Map_Location', max_length=255, blank=True, null=True)  # Field name made lowercase.
    org_name = models.CharField(db_column='Org_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taxonomic_groups = models.CharField(db_column='Taxonomic_Groups', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taxonomic_lineage = models.TextField(db_column='Taxonomic_lineage', blank=True, null=True)  # Field name made lowercase.
    symbol = models.TextField(db_column='Symbol', blank=True, null=True)  # Field name made lowercase.
    aliases = models.TextField(db_column='Aliases', blank=True, null=True)  # Field name made lowercase.
    all_gene_name = models.TextField(db_column='All_gene\x1f_name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    transcript_protein_name = models.CharField(db_column='Transcript_Protein_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ensembl_geneids = models.CharField(db_column='Ensembl_GeneIDs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ncbi_gene_id = models.IntegerField(db_column='NCBI_gene_ID', blank=True, null=True)  # Field name made lowercase.
    uniprot_id = models.CharField(db_column='Uniprot_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kegg_id = models.CharField(db_column='KEGG_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kegg_pathway = models.TextField(db_column='KEGG_pathway', blank=True, null=True)  # Field name made lowercase.
    cellular_component = models.TextField(db_column='Cellular_component', blank=True, null=True)  # Field name made lowercase.
    biological_process = models.TextField(db_column='Biological_process', blank=True, null=True)  # Field name made lowercase.
    molecular_function = models.TextField(db_column='Molecular_function', blank=True, null=True)  # Field name made lowercase.
    pfam_id = models.CharField(db_column='Pfam_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    protein_function = models.TextField(db_column='Protein_Function', blank=True, null=True)  # Field name made lowercase.
    string = models.CharField(db_column='String', max_length=255, blank=True, null=True)  # Field name made lowercase.
    alphafolddb = models.CharField(db_column='AlphaFoldDB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pdb = models.TextField(db_column='PDB', blank=True, null=True)  # Field name made lowercase.
    prosite = models.CharField(db_column='PROSITE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    interpro = models.TextField(db_column='InterPro', blank=True, null=True)  # Field name made lowercase.
    panther = models.CharField(db_column='PANTHER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cdd = models.TextField(db_column='CDD', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pathway = models.TextField(db_column='Pathway', blank=True, null=True)  # Field name made lowercase.
    animal_growth = models.CharField(db_column='Animal_growth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disease = models.CharField(db_column='Disease', max_length=255, blank=True, null=True)  # Field name made lowercase.
    plant_growth = models.CharField(db_column='Plant_Growth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stress = models.CharField(db_column='Stress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    orthology = models.TextField(db_column='Orthology', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'alldata'