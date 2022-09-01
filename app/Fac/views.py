from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json

import pyodbc
import mysql.connector
import requests
import urllib3

from Fac.models import Pedidos_Enca
from Fac.serializers import Pedidos_EncaSerializer

server= '200.105.238.146'
bd = 'ecom_bijoux_ec'
user = 'ecomp'
contrasena = 'B1j0@sw$!#'

try: 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+ contrasena)
    cursor = cnxn.cursor()
    print('conectado')
except:
    print('error')
    


from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def Pedidos_EncaApi(request,id=0):
    if request.method=='GET':
        pedidos_enca = Pedidos_Enca.objects.all()
        pedidos_enca_serializer=Pedidos_EncaSerializer(pedidos_enca,many=True)
        return JsonResponse(pedidos_enca_serializer.data,safe=False)       
    elif request.method=='POST':
        #pedidos_enca_data=JSONParser().parse(request)
        #pedidos_enca_serializer=Pedidos_EncaSerializer(data=pedidos_enca_data)
        #if pedidos_enca_serializer.is_valid():
           # pedidos_enca_serializer.save()
            #return JsonResponse("Agregado Correctamente",safe=False)
        #return JsonResponse("No se Agrego",safe=False)
        jd=json.loads(request.body)
        #print(jd['C_Empresa'])
        #jd.objects.create(C_Empresa=jd['C_Empresa'], N_Orden_Pedido=jd['N_Orden_Pedido'], F_Orden=jd['F_Orden'],C_Cod_Cliente=jd['C_Cod_Cliente'],C_Tipo_Envio=jd['C_Tipo_Envio'],C_Tipo_Identi=jd['C_Tipo_Identi'],Num_Identi=jd['Num_Identi'],D_Nom_Cliente=jd['D_Nom_Cliente'],D_Ape_Cliente=jd['D_Ape_Cliente'],x=jd['Direccion_Envio'],Dato_Ref1=jd['Dato_Ref1'],C_Ciudad=jd['C_Ciudad'],Cod_Postal=jd['Cod_Postal'],Tel1=jd['Tel1'],Contacto_mail=jd['Contacto_mail'],C_Tipo_Pago=jd['C_Tipo_Pago'],Num_Aprobacion=jd['Num_Aprobacion'],V_Fletes=jd['V_Fletes'],Estado_Cliente=jd['Estado_Cliente'],F_Grabacion=jd['F_Grabacion'],Url_Aprobacion=jd['Url_Aprobacion'],C_Lider=jd['C_Lider'],Estado_Proceso=jd['Estado_Proceso'])
        
        cur = cnxn.cursor()
        cur.execute("INSERT INTO Fac_Pedidos_Enca(Estado_Cliente,C_Cod_Cliente,Tel1,Contacto_mail,D_Ape_Cliente,Num_Identi,C_Tipo_Identi,C_Tipo_Envio,D_Nom_Cliente,C_Lider,C_Empresa, N_Orden_Pedido,F_Grabacion,F_Orden,C_Ciudad,V_Fletes,Direccion_Envio,C_Tipo_Pago) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(jd['Estado_Cliente'],jd['C_Cod_Cliente'],jd['Tel1'],jd['Contacto_mail'],jd['D_Ape_Cliente'],jd['Num_Identi'],jd['C_Tipo_Identi'],jd['C_Tipo_Envio'],jd['D_Nom_Cliente'],jd['C_Lider'],'3',jd['N_Orden_Pedido'],jd['F_Grabacion'],jd['F_Grabacion'],jd['C_Ciudad'],jd['V_Fletes'],jd['Direccion_Envio'],jd['C_Tipo_Pago']))
        cur.commit()

        #print(pedidos_enca_serializer)
        #print(request.body)
        
        pedidos_enca = {'message':"ingresado correctamente"}
        return JsonResponse(pedidos_enca)

    elif request.method=='PUT':
        pedidos_enca_data=JSONParser().parse(request)
        pedidos_enca=Pedidos_Enca.objects.get(N_Orden_Pedido=pedidos_enca_data['N_Orden_Pedido'])
        pedidos_enca_serializer=Pedidos_EncaSerializer(pedidos_enca,data=pedidos_enca_data)
        if pedidos_enca_serializer.is_valid():
            pedidos_enca_serializer.save()
            return JsonResponse("Actualizado",safe=False)
        return JsonResponse("Fallo")
    elif request.method=='DELETE':
        pedidos_enca=Pedidos_Enca.objects.get(N_Orden_Pedido=id)
        pedidos_enca.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def pedidos_encaApi(request,id=0):
    if request.method=='GET':
        pedidos_enca = Pedidos_Enca.objects.all()
        pedidos_enca_serializer=Pedidos_EncaSerializer(pedidos_enca,many=True)
        return JsonResponse(pedidos_enca_serializer.data,safe=False)
    elif request.method=='POST':
        pedidos_enca_data=JSONParser().parse(request)
        pedidos_enca_serializer=Pedidos_EncaSerializer(data=pedidos_enca_data)
        if pedidos_enca_serializer.is_valid():
            pedidos_enca_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        pedidos_enca_data=JSONParser().parse(request)
        pedidos_enca=Pedidos_Enca.objects.get(N_Orden_Pedido=pedidos_enca_data['N_Orden_Pedido'])
        pedidos_enca_serializer=Pedidos_EncaSerializer(pedidos_enca,data=pedidos_enca_data)
        if pedidos_enca_serializer.is_valid():
            pedidos_enca_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        pedidos_enca=Pedidos_Enca.objects.get(N_Orden_Pedido=id)
        pedidos_enca.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)