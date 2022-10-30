from rest_framework import viewsets
from apps.PushCase.api.serializers import PushcaseSerializer, PushcaseDetailSerializer

# Create your views here.
class PushcaseWiewSet(viewsets.ModelViewSet):
    serializer_class = PushcaseSerializer
    queryset = PushcaseSerializer.Meta.model.objects.filter(state=True)

class PushcaseDetailsWiewSet(viewsets.ModelViewSet):
    serializer_class = PushcaseDetailSerializer
    queryset = PushcaseSerializer.Meta.model.objects.all()
