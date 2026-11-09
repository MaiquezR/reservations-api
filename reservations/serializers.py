from .models import Resource, Reservation
from rest_framework import serializers


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'description', 'is_available']
    

class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    
    def validate(self, attrs):
        resource = attrs.get('resource')
        start = attrs.get('initial_date')
        end = attrs.get('final_date')

        if resource and start and end:
            overlap = Reservation.objects.filter(
                resource=resource,
                initial_date__lt=end,
                final_date__gt=start,
            ).exists()

            if overlap:
                raise serializers.ValidationError(
                    'This resource is already reserved in the given dates.'
                )

        return attrs
