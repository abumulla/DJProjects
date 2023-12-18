from django.db import models

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length=250,null=False)
    age = models.IntegerField()
    phone_no = models.IntegerField(max_length=10)
    email = models.EmailField(null=False,primary_key=True)
    password = models.CharField(max_length=300,null=False)

    def __str__(self):
        return self.email
