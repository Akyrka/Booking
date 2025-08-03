from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gmail = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Room(models.Model):
    number = models.CharField(max_length=100)
    peopl = models.CharField(max_length=10)
    

    def __str__(self):
        return f"Кімната {self.number} (на {self.peopl} осіб)"


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self):
        return f"{self.customer} → {self.room} з {self.start_time} до {self.end_time}"
