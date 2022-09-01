from django.db import models

# Create your models here.
class Pedidos_Enca(models.Model):
    N_Orden_Pedido = models.AutoField(primary_key=True)
    C_Empresa = models.IntegerField()
    F_Orden = models.CharField(max_length=500)
    C_Cod_Cliente = models.CharField(max_length=500)
    C_Tipo_Envio = models.CharField(max_length=500)
    C_Tipo_Identi = models.CharField(max_length=500)
    Num_Identi = models.CharField(max_length=500)
    D_Nom_Cliente = models.CharField(max_length=500)
    D_Ape_Cliente = models.CharField(max_length=500)
    Direccion_Envio = models.CharField(max_length=500)
    Dato_Ref1 = models.CharField(max_length=500)
    C_Ciudad = models.CharField(max_length=500)
    Cod_Postal = models.CharField(max_length=500)
    Tel1 = models.CharField(max_length=500)
    Contacto_mail = models.CharField(max_length=500)
    C_Tipo_Pago = models.CharField(max_length=500)
    Num_Aprobacion = models.CharField(max_length=500)
    V_Fletes = models.CharField(max_length=500)
    Estado_Cliente = models.CharField(max_length=500)
    F_Grabacion = models.CharField(max_length=500)
    Url_Aprobacion = models.CharField(max_length=500)
    C_Lider = models.CharField(max_length=500)
    Estado_Proceso = models.CharField(max_length=500)
    