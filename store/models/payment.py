from django.db import models

class Payment(models.Model): 
    atm = models.CharField(max_length=15)
    cvv = models.CharField(max_length=3)
    date = models.CharField(max_length=12)
    
    name = models.CharField(max_length=50)

    def register(self):
        self.save()
    