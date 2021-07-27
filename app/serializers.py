import re
from ast import literal_eval

from rest_framework import serializers

from .models import Points


class PointsSerializers(serializers.ModelSerializer):
    """
    Contains serialier fields and validation functions.
    """
    # closest_point = serializers.CharField(required=False)
    relative_point = serializers.CharField(allow_blank=True)
    points_submitted = serializers.CharField(allow_blank=True)

    class Meta:
        model=Points
        fields=['points_submitted','relative_point']
    def validate_relative_point(self,relative_point):
        """
        Validates the relative point
        """
        relative_point_re_pattern=re.compile('\(.*\,.*\)$')
        if relative_point_re_pattern.match(relative_point) == None:
            raise serializers.ValidationError({"error": "relative should folow this format (x,y)"})
        return relative_point
    def validate_points_submitted(self,points_submitted):
        try:

            return points_submitted
        except Exception as e:
            raise serializers.ValidationError({"error": "points submitted should folow this format-(2,3), (1,1), (5, 4), ..."})


class GetPointsSerializers(serializers.ModelSerializer):
    """
    Contains serialier fields for get endpoint.
    """
    closest_point = serializers.CharField(required=False)
    relative_point = serializers.CharField(allow_blank=True)
    points_submitted = serializers.CharField(allow_blank=True)

    class Meta:
        model=Points
        fields=['points_submitted','relative_point','closest_point']