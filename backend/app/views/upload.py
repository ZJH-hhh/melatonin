from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.newdata import Newdata
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class UploadView(APIView):
    file_headers = settings.MEDIA_ROOT
    url_headers = settings.ROOT_URL + settings.MEDIA_URL

    def post(self, request):
        try:
            file = request.FILES['file']

            fs = FileSystemStorage(location=os.path.join(self.file_headers, 'uploads'))

            filename = fs.save(file.name, file)
            
            return Response({
                'result': 'success',
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })

