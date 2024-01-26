from django.views import generic, View
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
class BikeListView(generic.ListView):
    model = Bike
    template_name = "shop/bikes.html"
    context_object_name = "bikes"
    queryset = Bike.objects.all()

    def get_queryset(self):
        return Bike.objects.all()


class BikeView(View):

    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        bike = Bike.objects.get(pk=pk)
        basket = Basket.objects.get(pk=1)
        return render(request, "shop/detail.html", {"bike": bike, "basket": basket})

    def post(self, request, pk, *args, **kwargs):
        pk = self.kwargs["pk"]
        bike = Bike.objects.get(pk=pk)

        seat = Seat.objects.get(id=bike.seat.pk)
        seat.quantity -= 1
        seat.save()

        tire = Tire.objects.get(id=bike.tire.pk)
        tire.quantity -= 2
        tire.save()

        frame = Frame.objects.get(id=bike.frame.pk)
        frame.quantity -= 1
        frame.save()

        if bike.has_basket is True:
            basket = Basket.objects.first()
            basket.quantity -= 1
            basket.save()

        name = request.POST['name']
        surname = request.POST['surname']
        phone = request.POST['phone_number']
        order = Order(bike=bike, name=name, surname=surname, phone_number=phone)
        order.save()

        return redirect(f"/order/{order.pk}")


class OrderDetailView(generic.DetailView):
    model = Order
    context_object_name = "order"
    template_name = "shop/order.html"
