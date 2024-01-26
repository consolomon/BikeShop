from django.db import models


# write your models here
class Frame(models.Model):
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.color}"


class Seat(models.Model):
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.color}"


class Tire(models.Model):
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.type}"


class Basket(models.Model):
    quantity = models.IntegerField()

    def __str__(self):
        return "Bike basket"


class Bike(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField()
    has_basket = models.BooleanField()

    def __str__(self):
        if self.has_basket is True:
            return f"{self.name} (with basket)"
        else:
            return f"{self.name}"

    def get_basket(self):
        return "yes" if self.has_basket is True else "no"

    def is_available(self):
        if self.frame.quantity < 1:
            return False
        elif self.seat.quantity < 1:
            return False
        elif self.tire.quantity < 2:
            return False
        else:
            return True


class Order(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    status = models.CharField(max_length=1)

    def __str__(self):
        return f"Order number {self.pk}: {self.bike}"