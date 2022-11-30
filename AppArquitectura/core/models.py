from django.db import models

# Create your models here.

class Categoria (models.Model): 
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Mascota')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Tipo de mascota')

    def __str__(self):
        return self.nombreCategoria


class Categoria2 (models.Model): 
    idCategoria2 = models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria2= models.CharField(max_length=50, verbose_name='Nombre de Categoría')

    def __str__(self):
        return self.nombreCategoria2

class Usuarios(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre de usuario')
    email = models.CharField(max_length=40,primary_key=True, verbose_name='Email')
    numero =models.CharField(max_length=10, verbose_name='Fono')
    passs =models.CharField(max_length=10,  verbose_name='rut')
    dire =models.CharField(max_length=100,  verbose_name='Dirección')
    categoria2=models.ForeignKey(Categoria2, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

class SolicitudEquipoeInsumos(models.Model):
    n_pabellon = models.CharField(max_length=10, primary_key=True, verbose_name='Numero de pabellon')
    nombre = models.CharField(max_length=40, verbose_name='Nombre de identificación')
    equipo = models.CharField(max_length=300, verbose_name='Equipo que se solicita')
    insumo = models.CharField(max_length=300, verbose_name='Insumos que se solicita')
    msg = models.CharField(max_length=300, verbose_name='Comentario Adicional')

class Categoria3 (models.Model): 
    id_condicion = models.IntegerField(primary_key=True, verbose_name='Id de Condicion')
    nombre_condicion = models.CharField(max_length=50, verbose_name='Condicion Si o No')

    def __str__(self):
        return self.nombre_condicion

class PabellonEnCondiciones(models.Model):
    n_pabellon = models.CharField(max_length=10, primary_key=True, verbose_name='Numero de pabellon')
    c_infra = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    c_equipo = models.ForeignKey(Categoria2, on_delete=models.CASCADE)
    c_rrhh = models.ForeignKey(Categoria3, on_delete=models.CASCADE)
    msg = models.CharField(max_length=300, verbose_name='Comentario adicional')

    def __str__(self):
        return self.n_pabellon



