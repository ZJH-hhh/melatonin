from rest_framework.views import APIView
from rest_framework.response import Response
from app.models.suggestion import Suggestion

class SuggestionView(APIView):
    def post(self, request):
        try:
            params = request.data.get('params', {})
            email = params.get('email')
            subject = params.get('subject')
            message = params.get('message')

            suggestion = Suggestion.objects.create(
                email=email,
                subject=subject,
                message=message
            )
            
            return Response({
                'result': 'success',
            })
        except Exception as e:
            return Response({
                'result': str(e)
            })

