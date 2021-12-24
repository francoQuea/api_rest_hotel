from rest_framework import serializers
from hotel_api.models import State, Room, Client, Invoice, Payment, Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    state = ReservationSerializer(read_only=True, many=True)
    class Meta:
        model = State
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    invoice = ReservationSerializer(read_only=True, many=True)
    class Meta:
        model = Invoice
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    #client1 = ReservationSerializer(read_only=True, many=True)
    client2 = InvoiceSerializer(read_only=True, many=True)
    class Meta:
        model = Client
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    room = ReservationSerializer(read_only=True, many=True)
    class Meta:
        model = Room
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    payment = ReservationSerializer(read_only=True, many=True)
    class Meta:
        model = Payment
        fields = '__all__'
