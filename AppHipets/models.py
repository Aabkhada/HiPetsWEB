from django.db import models

# Create your models here.
class Mascota(models.Model):
    mascota = models.CharField(max_length=120)
    class Meta:
        db_table = "mascota"
    def __str__(self):
        return u'{0}'.format(self.mascota)
        
class Tipo(models.Model):
    tipo = models.CharField(max_length=100)
    class Meta:
        db_table = "tipo"
    def __str__(self):
        return u'{0}'.format(self.tipo)

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300)
    info = models.CharField(max_length=600)
    precio = models.IntegerField()
    img = models.ImageField(default='default')
    mascota = models.ForeignKey(Mascota,on_delete=models.CASCADE,default='')
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE,default='')
    class Meta:
        db_table = "producto"

class Formulario(models.Model):
    id_formulario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 200)
    email = models.CharField(max_length=300)
    file = models.FileField(upload_to='pdf/')
    class Meta:
        db_table = "formulario"