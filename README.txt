JUSTIFICACION DE LA CREACION DE LOS ENDPOINTS PARA LA API DE RESERVAS DE HOTEL

La creación de los Endpoints la implementé usando los viewsets de rest_framework, 
porque considero que los viewsets de rest_framework, son la manera más práctica y 
sencilla de implementar, obteniendo con poco código y en corto tiempo una API 
lista para consumir por aplicaciones de terceros.

EL PORQUÉ DE LOS ENDPOINTS

He creado un total de 6 endpoints, un endpoint por cada entidad de los modelos 
que existen en la base de datos, estos modelos y sus URLs(endpoints) respectivas son los siguientes:

- State: http://127.0.0.1:8000/state/
- Room: http://127.0.0.1:8000/room/
- Client: http://127.0.0.1:8000/client/
- Invoice: http://127.0.0.1:8000/invoice/
- Payment: http://127.0.0.1:8000/payment/
- Reservation: http://127.0.0.1:8000/reservation/

Se creo cada endpoint para cada entidad que permitirá el registro de información necesaria en cada endpoint
para poder trabajar al final con el endpoint que nos interesa que es el de Reservation(http://127.0.0.1:8000/reservation/).

La entidad de Client(Cliente) tiene relacion con Invoice(Factura) y a su vez Invoice tiene relación con 
Reservation(Reservacion) de esta manera al saber el número de factura, también se sabrá el número de documento
del cliente.

La entidad State(Estado) tiene relación con Reservatión para que se pueda apreciar el estado de la reservación
La entidad Room(Habitación) tiene relacion con Reservation para que se identifique el número que hablitación se va a reservar.
La entidad Payment(Método de pago) tiene relación con Reservation para que se vea el método de pago que se va a utilizar para
pagar por el servicio.

La entidad Reservation como tal es la que almacena todos los datos referentes a la reservación como ser: 
días de estancia, monto pagado, día en se tomará la reserva, datos de la habitación, número de factura, número de
documento del cliente, método de pago y por último el estado de la reservación.

Se me dió directrices para este ejercicio en las cuales no estaba contemplado las entidades de State, 
Room, Client, Invoice, Payment pero he considerado para esta práctica que debe estar estructurado de 
esta manera, porque es una buena práctica y una buena manera de manejar la información en una aplicación,
utilizando la normalización de bases de datos como herramienta principal.

Tanto como el endpoint de Reservation como los demás endpoints están listos para consumirse ya sea por 
aplicaciones propias del sistema como también aplicaciones de terceros.



