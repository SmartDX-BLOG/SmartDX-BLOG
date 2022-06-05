from django.db import models

# Create your models here.


class Usr(models.Model):
    usr_sno = models.AutoField(primary_key=True)
    id = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    nm = models.CharField(max_length=100)
    eml = models.CharField(max_length=100)
    sgnup_dt = models.DateField()

    def _str_(self):
        return self.usr_sno
