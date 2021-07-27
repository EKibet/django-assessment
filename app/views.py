from django.shortcuts import render
from rest_framework import status

import math
import pdb

from django.http import response

import numpy as np
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Points
from ast import literal_eval
from .serializers import PointsSerializers,GetPointsSerializers

class GetPairs(GenericAPIView):
    """A GenericAPIView that computes the closest pair of points from a string of points

    Args:
        points_submitted- type(String),closest_point - type(String) and relative_point- type(String)
    Output: Closest Point
    """
    serializer_class=PointsSerializers
    save_serializer_class=GetPointsSerializers
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data=serializer.validated_data
        try:
            data =list(literal_eval(validated_data.get('points_submitted')))
            arr_dimension= np.array(data)
            left_bottom = np.array(literal_eval(validated_data.get('relative_point',(0,0))))
            distances = np.linalg.norm(arr_dimension-left_bottom, axis=1)
            min_index = np.argmin(distances)
            calculated_closest_point=arr_dimension[min_index]
            serializer.save(closest_point=calculated_closest_point)
            message=f"Closest point is {calculated_closest_point}, at a distance of {distances[min_index]}"
            return Response({'Response':message})
        except Exception as e:
            return Response({'error':f'{e}'},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        queryset=Points.objects.all()
        serialized_queryset=self.save_serializer_class(queryset,many=True)
        return Response({'saved_points':serialized_queryset.data})

def handler404(request, exception, template_name="404.html"):
    response = render(template_name)
    response.status_code = 404
    return response
