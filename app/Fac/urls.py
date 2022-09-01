from django.conf.urls import url
from Fac import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
   
   
    url(r'^Pedidos_Enca$',views.Pedidos_EncaApi),
    url(r'^Pedidos_Enca/([0-9]+)$',views.Pedidos_EncaApi),

 url(r'^Fac/savefile',views.SaveFile)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)