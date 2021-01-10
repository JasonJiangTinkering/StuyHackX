from rest_framework import viewsets
from school.models import School
from school.serializers import SchoolSerializer
from rest_framework.response import Response

# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

    def list(self, request):
        queryset = sorted(School.objects.all(), key=lambda t: -t.school_score)
        serializer = SchoolSerializer(queryset, many=True)
        return Response(serializer.data)