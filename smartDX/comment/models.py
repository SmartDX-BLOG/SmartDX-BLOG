from django.db import models
from user.models import Usr
from board.models import Brd

# Create your models here.
class Commnt(models.Model):
    commnt_sno = models.AutoField(primary_key=True)
    usr_sno = models.ForeignKey(Usr, on_delete=models.CASCADE, db_column='usr_sno')
    contnt = models.CharField(max_length=300)
    dt = models.DateField()
    brd_sno = models.ForeignKey(Brd, on_delete=models.CASCADE, db_column='brd_sno')

    def _str_(self):
        return self.commnt_sno