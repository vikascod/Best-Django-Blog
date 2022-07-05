from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

