from rest_framework import serializers
from Fac.models import Pedidos_Enca



class Pedidos_EncaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pedidos_Enca
        fields=('C_Empresa','N_Orden_Pedido','F_Orden','C_Cod_Cliente', 'C_Tipo_Envio','C_Tipo_Identi', 'Num_Identi','D_Nom_Cliente','D_Ape_Cliente','Direccion_Envio','Dato_Ref1','C_Ciudad','Cod_Postal','Tel1','Contacto_mail','C_Tipo_Pago','Num_Aprobacion','V_Fletes','Estado_Cliente','F_Grabacion','Url_Aprobacion','C_Lider','Estado_Proceso')     

