from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiview(APIView):
    """Test API Views"""

    def get(self, request, format=None):
        """Returns a list of API view features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URls',
        ]

        return Response({'message': 'Hellow', 'an_apiview': an_apiview})

