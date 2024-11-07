from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.Alldata import Alldata
from app.models.experimental import AnimalTest, PlantTest


class ExpermentalView(APIView):
    def get(self, request):
        try:
            database_id = request.GET.get('magdb_id')
            gene_id = Alldata.objects.filter(database_id=database_id).values_list('gene_id', flat=True).first()

            data = []
            animal_test = AnimalTest.objects.filter(gene_id=gene_id).values().first()
            if animal_test:
                data.append(animal_test)
            plant_data = PlantTest.objects.filter(gene_id=gene_id).values().first()
            if plant_data:
                data.append(plant_data)

            return Response({
                'result': 'success',
                'data': data
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })