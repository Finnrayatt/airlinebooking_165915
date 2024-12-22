from rest_framework import viewsets
from .models import Flight, Passenger
from .serializers import FlightSerializer, PassengerListSerializer, PassengerCreateSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PassengerCreateSerializer
        return PassengerListSerializer