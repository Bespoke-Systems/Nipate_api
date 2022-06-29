from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from locations.models import TownsModel, CountyModel
from locations.serializers import TownsModelSerializer, CountyModelSerializers


class CountyView(APIView):

    def get(self, request):
        counties = CountyModel.objects.all()
        serializer = CountyModelSerializers(counties, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TownsView(APIView):

    CountyID = openapi.Parameter('CountyID', openapi.IN_QUERY, description="Search by CountyID(optional)", type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(operation_description="Endpoint for searching town loactions", manual_parameters=[CountyID], responses={200: TownsModelSerializer(many=True)})
    def get(self, request):
        data = request.query_params
        try:
            towns = TownsModel.objects.filter(CountID_id=data["CountyID"])
            serializer = TownsModelSerializer(towns, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            pass
        towns = TownsModel.objects.all()
        serializer = TownsModelSerializer(towns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
