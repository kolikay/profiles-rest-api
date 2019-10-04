from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
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



class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """Returns a Hello message"""
        a_viewset = [
        'Uses action list, create, retrive, update, partial_update',
        'Automatically maps to Urls using Routers',
        'Provides more functionality with less codes',
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})


    def create(self, request):
        """Create a new hello message"""
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

    def retrive(self, request, pk=None):
        """Handles getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handles updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """handles removing an obbject"""
        return Response({'http_method ':'DELETE'})



