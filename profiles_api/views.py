from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloAPIView(APIView):
    """Testing API View"""
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Return a list of API views features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch,put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
            ]
        return Response({'message':'hello', 'an_apiview':an_apiview})


    def post(self, request):
        """Create a hello with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response ({'massage':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handles a partial update an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


