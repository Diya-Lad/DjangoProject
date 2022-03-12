from django.db import models

# Create your models here.
class login(models.Model):
    firstname = models.CharField(max_length=50,default='')
    lastname = models.CharField(max_length=50,default='')
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50,default='')
    role = models.CharField(max_length=50,default='')

class importantDocuments(models.Model):
    email = models.ForeignKey(login,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50,default='')
    document = models.FileField()

    @property
    def email(self):
        return self.email

    