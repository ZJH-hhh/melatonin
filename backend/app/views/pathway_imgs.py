from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.Alldata import Alldata
from django.conf import settings
from django.core.paginator import Paginator
import re

class PathwayView(APIView):
    url_headers = settings.ROOT_URL + settings.MEDIA_URL

    def get(self, request):
        try:
            database_id = request.GET.get('magdb_id')
            pagesize = request.GET.get('pageSize', 10)
            page = request.GET.get('page', 1)

            pathways = Alldata.objects.filter(database_id=database_id).values_list('kegg_pathway', flat=True).first()
            if pathways:
                pathways = pathways.split(',')

            pathway_img = []
            if pathways:
                for item in pathways:
                    pathway_img.append(self.url_headers + 'image/kegg_image/' + item + '.png')
            
            paginator = Paginator(pathway_img, pagesize)

            current_page = paginator.page(page)
            res = list(current_page.object_list)

            return Response({
                'result': 'success',
                'total': paginator.count,
                'data': res
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })

