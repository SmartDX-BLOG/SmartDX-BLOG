from django.db import models
from user.models import Usr

# Create your models here.
class Brd(models.Model):
    brd_sno = models.AutoField(primary_key=True)
    usr_sno = models.ForeignKey(Usr, on_delete=models.CASCADE, db_column='usr_sno')
    ttl = models.CharField(max_length=100)
    cntnt = models.CharField(max_length=300)
    dt = models.DateField()
    clck = models.IntegerField(default=0)

    def _str_(self):
        return self.brd_sno

class Fl(models.Model):
    fl_sno = models.AutoField(primary_key=True)
    brd_sno = models.ForeignKey(Brd, on_delete=models.CASCADE, db_column='brd_sno')
    usr_sno = models.ForeignKey(Usr, on_delete=models.CASCADE, db_column='usr_sno')
    orgnl_fnm = models.CharField(max_length=100)
    fnm = models.CharField(max_length=150)

    def _str_(self):
        return self.fl_sno
