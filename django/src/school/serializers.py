from rest_framework import serializers
from school.models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            'name',
            'school_score'
        ]