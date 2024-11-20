# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AnimalTest(models.Model):
    gene_id = models.CharField(db_column='ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    background = models.TextField(db_column='Background', blank=True, null=True)  # Field name made lowercase.
    problem = models.CharField(db_column='Problem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    object_and_group = models.TextField(db_column='Object and group', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    conclusion = models.TextField(db_column='Conclusion', blank=True, null=True)  # Field name made lowercase.
    gene_intervention = models.CharField(db_column='Gene intervention', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    result = models.TextField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    treatment = models.TextField(db_column='Treatment', blank=True, null=True)  # Field name made lowercase.
    treatment_result = models.TextField(db_column='Treatment Result', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    referrence = models.CharField(db_column='Referrence', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doi = models.CharField(db_column='DOI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'animal_test'


class PlantTest(models.Model):
    gene_id = models.CharField(db_column='ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    background = models.TextField(db_column='Background', blank=True, null=True)  # Field name made lowercase.
    problem = models.CharField(db_column='Problem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conclusion_details = models.TextField(db_column='Conclusion details', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    conclusion = models.TextField(db_column='Conclusion', blank=True, null=True)  # Field name made lowercase.
    gene_intervention = models.CharField(db_column='Gene intervention', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    result = models.TextField(db_column='Result', blank=True, null=True)  # Field name made lowercase.
    treatment = models.CharField(db_column='Treatment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    treatment_site = models.CharField(db_column='Treatment site', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tratment_result = models.TextField(db_column='Tratment result', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pubmed_id = models.CharField(db_column='PubMed ID', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    doi = models.CharField(db_column='DOI', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plant_test'
