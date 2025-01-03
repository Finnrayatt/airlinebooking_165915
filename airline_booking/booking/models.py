from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.flight_number} - {self.origin} to {self.destination}"

class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='passengers')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
