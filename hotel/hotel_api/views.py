from hotel_api.models import State, Room, Client, Invoice, Payment, Reservation
from hotel_api.serializers import StateSerializer, RoomSerializer, ClientSerializer, InvoiceSerializer, PaymentSerializer, ReservationSerializer
from rest_framework import viewsets

class StateApi(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class RoomApi(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class ClientApi(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class InvoiceApi(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class PaymentApi(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class ReservationApi(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
