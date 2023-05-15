from django.db import models

# Create your models here.
class Carreer(models.Model):
    clave = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecalt = models.DateField(auto_now_add=True)
    fecbaj = models.DateField(null=True, default=None)
    
    class Meta:
        managed = True
        db_table = 'carrera'

class Subject(models.Model):
    clave = models.IntegerField(primary_key=True)
    descri = models.CharField(max_length=100)
    nsesio = models.IntegerField()
    durses = models.FloatField()
    taller = models.IntegerField(null=True, default=None)
    fecalt = models.DateField(auto_now_add=True)
    fecbaj = models.DateField(null=True, default=None)
    tipo = models.CharField(max_length=1)
    
    class Meta:
        managed = True
        db_table = 'materia'
        
class Plan(models.Model):
    clave = models.CharField(max_length=1)
    carrer = models.ForeignKey(Carreer, on_delete=models.CASCADE)
    materi = models.ForeignKey(Subject, on_delete=models.CASCADE)
    fecalt = models.DateField(auto_now_add=True)
    fecbaj = models.DateField(null=True, default=None)
    area = models.CharField(max_length=50, null=True, default=None)
    reqsim = models.IntegerField(null=True, default=None)
    requi1 = models.IntegerField(null=True, default=None)
    requi2 = models.IntegerField(null=True, default=None)
    requi3 = models.IntegerField(null=True, default=None)
    requi4 = models.IntegerField(null=True, default=None)
    semest = models.IntegerField()
    
    class Meta:
        managed = True
        db_table = 'plan'
        