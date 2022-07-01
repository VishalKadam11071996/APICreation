from django.db import models



class PatientsModel(models.Model):
    name = models.CharField(max_length=50)
    claim = models.CharField(max_length=100)
    gvt_id = models.CharField(max_length=20)

    def __str__(self):
        return self.name
