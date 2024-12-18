# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bacteria(models.Model):
    tax_id = models.CharField(max_length=255, blank=True, null=False, primary_key=True)
    org_name = models.CharField(db_column='Org_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bacteria'


class Fungi(models.Model):
    tax_id = models.IntegerField(blank=True, null=False, primary_key=True)
    org_name = models.CharField(db_column='Org_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fungi'


class Others(models.Model):
    tax_id = models.IntegerField(blank=True, null=False, primary_key=True)
    org_name = models.CharField(db_column='Org_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    count = models.IntegerField(db_column='Count', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'others'
