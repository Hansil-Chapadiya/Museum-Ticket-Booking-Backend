from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from backend.models import Museums
from .permission import HasSecretKey
from .serializers import MuseumSerializer
from rest_framework.exceptions import NotFound
from django.conf import settings
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from bson import ObjectId

@api_view(['GET'])
@permission_classes([HasSecretKey])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getMuseums(request):
    try:
        museum = Museums.objects.all()
        serializer = MuseumSerializer(museum, many=True)
        response_data = serializer.data

        # if isinstance(response_data, list):
        #     for item in response_data:
        #         if isinstance(item, dict):
        #             item.pop('_id', None)
        # else:
        #     return Response({
        #         'status': False,
        #         'detail': 'isinstance not a dictionary or in json'
        #     })

        return Response({
            'status': True,
            'data': response_data
        })
    except Exception as e:
        return Response({
                'status': False,
                'detail': str(e)
        })

@api_view(['POST'])
@permission_classes([HasSecretKey])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def addMuseum(request):
    try:
        serializer = MuseumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            # if isinstance(response_data, dict):
            #     response_data.pop('_id', None)
            return Response({
                'status': True,
                'data': response_data
            })
        else:
            return Response({
                'status': False,
                'detail': serializer.errors
            })
    except Exception as e:
        return Response({
                'status': False,
                'detail': str(e) + ' or Museum already exist'
        })

@api_view(['GET'])
@permission_classes([HasSecretKey])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getMuseum(request, id):
    try:
        museum = Museums.objects.get(_id=ObjectId(id))
        serializer = MuseumSerializer(museum)
        response_data = serializer.data

        if isinstance(response_data, dict):
            response_data.pop('_id', None)
        else:
            return Response({
                'status': False,
                'detail': 'isinstance not a dictionary or in json'
            })

        return Response({
            'status': True,
            'data': response_data
        })
    except Exception as e:
        return Response({
                'status': False,
                'detail': str(e) + 'or Museum not found'
        })

@api_view(['PUT'])
@permission_classes([HasSecretKey])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def updateMuseum(request, id):
    try:
        # Fetch the existing museum object
        museum = Museums.objects.get(_id=ObjectId(id))

        # Create a serializer instance with the existing data and updated data
        serializer = MuseumSerializer(museum, data=request.data, partial=True)

        # Validate and save the data
        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            # if isinstance(response_data, dict):
            #     response_data.pop('_id', None)
            return Response({
                'status': True,
                'data': response_data
            })
        else:
            return Response({
                'status': False,
                'detail': serializer.errors
            })
    except Museums.DoesNotExist:
        raise NotFound(detail="Museum not found")
    except Exception as e:
        return Response({
            'status': False,
            'detail': str(e) + ' or Museum could not be updated'
        })