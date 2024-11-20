from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.newdata import Newdata

class NewdataView(APIView):
    def post(self, request):
        try:
            params = request.data.get('params', {})
            species = params.get('species')
            gene_name = params.get('gene_name')
            sequence = params.get('sequence')
            reference = params.get('reference')
            external_link = params.get('external_link')
            email = params.get('email')

            newdata = Newdata.objects.create(
                species=species,
                gene_name=gene_name,
                sequence=sequence,
                reference=reference,
                external_link=external_link,
                email=email
            )
            
            return Response({
                'result': 'success',
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })

