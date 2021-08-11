from django.db import models



class InsertToDb(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    phone_number = models.IntegerField()
    

    
    