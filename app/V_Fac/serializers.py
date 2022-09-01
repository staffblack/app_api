from rest_framework import serializers
from V_Fac.models import V_Fac_ClientesB5

class V_Fac_ClientesB5Serializer(serializers.ModelSerializer):
    class Meta:
        model=V_Fac_ClientesB5
        fields=('C_Empresa','C_Tipo_Identi','C_Cod_Cliente','D_Nom_Cliente','D_Nom2_Cliente','D_Ape_Cliente', 'D_Ape2_Cliente','Cliente','Direccion_Clien','C_Ciudad','N_Ciudad','C_Region','N_Region','C_Pais','N_Pais_Es','Cod_Postal','N_Cod_Postal','N_Sector','Tel1','Tel2','Contacto_mail', 'Cod_Operador_tel1','Nom_Operador','F_Ingreso','Ult_Fec_Fac','C_Lider','Lider','C_Vendedor','Vendedor','C_Director','Director','C_Regional','Regional','Flag_Vigente')     

    
