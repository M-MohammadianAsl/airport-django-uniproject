from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name + " " + self.last_name
    
class Airplane(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacity = models.IntegerField()
    code = models.IntegerField()

    def __str__(self):
        return self.name + ", " + self.model
    
class Flight(models.Model):
    title = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    airplane = models.ForeignKey("Airplane", on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Ticket(models.Model):
    title = models.CharField(max_length=50)
    reserver_name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    date = models.DateTimeField()
    flight = models.ForeignKey("Flight", on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.title
    

