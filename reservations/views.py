from rest_framework import permissions, viewsets

from .models import Reservation, Resource
from .serializers import ReservationSerializer, ResourceSerializer


# Create your views here.
class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user).select_related('resource')
    