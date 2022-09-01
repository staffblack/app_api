from django.conf.urls import url
from V_Fac import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
   
   
    url(r'^V_Fac_ClientesB5$',views.V_Fac_ClientesB5Api),
    #url(r'^Pedidos_Enca/([0-9]+)$',views.Pedidos_EncaApi),

 url(r'^V_Fac/savefile',views.SaveFile)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)