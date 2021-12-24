from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("state", viewset = views.StateApi)
router.register("room", viewset = views.RoomApi)
router.register("client", viewset = views.ClientApi)
router.register("invoice", viewset = views.InvoiceApi)
router.register("payment", viewset = views.PaymentApi)
router.register("reservation", viewset = views.ReservationApi)

urlpatterns = [
    path('', include(router.urls)), 
]