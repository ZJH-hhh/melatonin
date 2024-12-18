from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.Alldata import Alldata
from django.core.paginator import Paginator
from django.conf import settings
import os


class DiseaseView(APIView):
    file_headers = settings.MEDIA_ROOT
    url_headers = settings.ROOT_URL + settings.MEDIA_URL

    def get(self, request):
        try:
            pagesize = request.GET.get('pageSize', 10)
            page = request.GET.get('page', 1)

            folder_path = os.path.join(self.file_headers, 'image/animal_disease/')
            file_paths = []
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(self.url_headers, 'image/animal_disease/', file_name)
                name, _ = os.path.splitext(file_name)
                file_paths.append((name, file_path))

            paginator = Paginator(file_paths, pagesize)
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

