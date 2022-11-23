from django.shortcuts import render
from django.http import HttpResponse
from .models import Familia
from appFamilia.models import Familia
from django.template import loader
# Create your views here.


def familia(request):
    miPadre = Familia(nombre = "Pablo Alejandro Lobo", fecha_nac ="1964-08-31", doc = 17222222)
    miMadre = Familia(nombre = "Priscila Olga Witoszek", fecha_nac = "1968-07-23", doc = 20222222)
    miSobrino1 = Familia(nombre = "Miles Nehemias Lobo", fecha_nac = "2021-09-09", doc = 50222222)
    miSobrino2 = Familia(nombre = "Felipe Lobo", fecha_nac = "2022-01-27", doc = 50333333)

    miPadre.save()
    miMadre.save()
    miSobrino1.save()
    miSobrino2.save() 


    dic = {
        "nombre_miPadre": miPadre.nombre,
        "fechanac_miPadre": miPadre.fecha_nac,
        "doc_miPadre": miPadre.doc,
        "nombre_miMadre": miMadre.nombre,
        "fechanac_miMadre": miMadre.fecha_nac,
        "doc_miMadre": miMadre.doc,        
        "nombre_miSobrino1": miSobrino1.nombre,
        "fechanac_miSobrino1": miSobrino1.fecha_nac,
        "doc_miSobrino1": miSobrino1.doc,
        "nombre_miSobrino2": miSobrino2.nombre,
        "fechanac_miSobrino2": miSobrino2.fecha_nac,
        "doc_miSobrino2": miSobrino2.doc
        }
    #Diccionario del cual se van a sacar los datos para el HTML (Voy a usar la clave siempre)
    
    plantilla = loader.get_template("template1.html") #Llamo al template (Ojo con el nombre)
    doc = plantilla.render(dic)

    return HttpResponse(doc) #Documento que va a devolver  