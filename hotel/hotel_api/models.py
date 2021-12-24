from django.db import models

class State(models.Model):
    id_state = models.AutoField(primary_key=True)
    name_state = models.CharField(max_length=20)

    def __str__(self):
        row = self.name_state
        return row

class Room(models.Model):
    num_room = models.CharField(max_length=20, primary_key=True)
    description = models.TextField(max_length=250)

    def __str__(self):
        row = self.num_room
        return row

class Client(models.Model):
    doc_client = models.IntegerField(primary_key=True)
    name_client = models.CharField(max_length=50)
    num_phone = models.IntegerField()

    def __str__(self):
        row = self.name_client
        return row

class Invoice(models.Model):
    num_invoice = models.CharField(max_length=50, primary_key=True)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    client_id = models.ForeignKey(Client, related_name="client", on_delete=models.CASCADE)

    def __str__(self):
        row = self.num_invoice
        return row

class Payment(models.Model):
    id_payment = models.AutoField(primary_key=True)
    method_payment = models.CharField(max_length=100)

    def __str__(self):
        row = self.method_payment
        return row

class Reservation(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    stay_days = models.IntegerField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    room_num = models.ForeignKey(Room, related_name="room", on_delete=models.CASCADE)
    invoice_num = models.ForeignKey(Invoice, related_name="invoice", on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, related_name="payment", on_delete=models.CASCADE)
    state_id = models.ForeignKey(State, related_name="state", on_delete=models.CASCADE)
    reserv_date = models.DateField()
