from django.db import models

class Transaction(models.Model):
    title = models.CharField(max_length=100)    
    amount = models.FloatField()                
    type = models.CharField(max_length=10)      
    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.title} - {self.amount}"
